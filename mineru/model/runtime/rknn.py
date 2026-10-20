# Copyright (c) Opendatalab. All rights reserved.
"""RK3588 NPU 推理会话（rknn-toolkit-lite2），接口与 runtime/onnx.py 对齐。

消费者只依赖三件事：``get_inputs()`` / ``get_outputs()`` 返回带 ``name`` 与
``shape`` 的节点描述；``run(output_names, input_feed)`` 按输入名喂入并返回
ndarray 列表。RKNNLite 仅接受位置输入，多输入模型的输入顺序与固定输入形状
由转换管线在 .rknn 同目录写出的 ``<model>.rknn.inputs.json`` 声明
（``{"input_names": [...], "input_size": [[...]]}``；历史上只有名字数组的
旧格式仍可读，但没有形状）。输出形状在加载时用零输入探测一次获得。
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from loguru import logger

__all__ = ["RknnSession", "RknnUnavailableError", "rknn_available", "rknn_session"]

_CORE_MASK_ENV = "MINERU_RKNN_CORE_MASK"
_INPUT_NAMES_SUFFIX = ".inputs.json"


class RknnUnavailableError(RuntimeError):
    """当前环境不具备 RKNN 运行时（非 RK3588 板或未安装 rknn-toolkit-lite2）。"""


@dataclass(frozen=True)
class _IONode:
    """与 onnxruntime NodeArg 对齐的最小节点描述，消费者读取 ``name`` 与 ``shape``。"""

    name: str
    shape: tuple[int, ...] | None = None


def rknn_available() -> bool:
    """仅探测 rknnlite 是否可导入，不初始化 NPU。"""
    from .device import module_available

    return module_available("rknnlite")


def _load_sidecar(model_path: Path) -> tuple[list[str], list[list[int]]]:
    """读取转换管线写出的输入清单（名字 + 固定形状）；不存在时返回两个空列表。"""
    sidecar = model_path.parent / (model_path.name + _INPUT_NAMES_SUFFIX)
    if not sidecar.is_file():
        return [], []
    data = json.loads(sidecar.read_text(encoding="utf-8"))
    if isinstance(data, list):  # 旧格式：仅有输入名数组。
        if not all(isinstance(name, str) for name in data):
            raise ValueError(f"Invalid RKNN input name list: {sidecar}")
        return list(data), []
    if not isinstance(data, dict):
        raise ValueError(f"Invalid RKNN inputs sidecar: {sidecar}")
    names = data.get("input_names")
    sizes = data.get("input_size") or []
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError(f"Invalid RKNN input name list: {sidecar}")
    return list(names), [list(size) for size in sizes]


class RknnSession:
    """RKNNLite 的 onnxruntime InferenceSession 风格封装。"""

    def __init__(self, model_path: str, *, core_mask: str | None = None) -> None:
        """加载 .rknn 并初始化 NPU 运行时；core_mask 取 auto/0/1/2/0_1_2。"""
        if not rknn_available():
            raise RknnUnavailableError(
                "rknn-toolkit-lite2 is not installed; the RKNN backend requires an RK3588 board with librknnrt."
            )
        from rknnlite.api import RKNNLite

        self.model_path = str(model_path)
        self._rknn = RKNNLite()
        if self._rknn.load_rknn(self.model_path) != 0:
            raise RknnUnavailableError(f"Failed to load RKNN model: {self.model_path}")
        masks = {
            "auto": RKNNLite.NPU_CORE_AUTO,
            "0": RKNNLite.NPU_CORE_0,
            "1": RKNNLite.NPU_CORE_1,
            "2": RKNNLite.NPU_CORE_2,
            "0_1_2": RKNNLite.NPU_CORE_0_1_2,
        }
        mask_key = (core_mask or os.getenv(_CORE_MASK_ENV, "auto")).strip().lower()
        if mask_key not in masks:
            raise ValueError("MINERU_RKNN_CORE_MASK must be one of: auto, 0, 1, 2, 0_1_2")
        if self._rknn.init_runtime(core_mask=masks[mask_key]) != 0:
            raise RknnUnavailableError(f"Failed to initialize RKNN runtime for: {self.model_path}")
        input_names, input_sizes = _load_sidecar(Path(self.model_path))
        input_count, output_count = self._io_counts(len(input_names))
        names = [*(input_names or []), *[f"input_{i}" for i in range(input_count)]][:input_count]
        sizes = [*(input_sizes or []), *[None] * input_count][:input_count]
        self._input_sizes: list[list[int] | None] = sizes
        self._inputs = [
            _IONode(name, tuple(size) if size else None) for name, size in zip(names, sizes, strict=True)
        ]
        self._outputs = self._probe_output_shapes(output_count)
        logger.info(
            "RKNN ready: model={}, inputs={}, outputs={}, core_mask={}",
            Path(self.model_path).name,
            [(node.name, node.shape) for node in self._inputs],
            [(node.name, node.shape) for node in self._outputs],
            mask_key,
        )

    def _io_counts(self, known_inputs: int) -> tuple[int, int]:
        """优先用驱动查询到的输入/输出个数；不可用时按已知清单与单输出回退。"""
        getter = getattr(self._rknn, "get_in_out_num", None)
        if callable(getter):
            try:
                counts: dict[str, Any] = getter()
                return int(counts.get("n_input", known_inputs) or known_inputs or 1), int(counts.get("n_output", 1) or 1)
            except Exception:
                pass
        return known_inputs or 1, 1

    def _probe_output_shapes(self, output_count: int) -> list[_IONode]:
        """用 sidecar 声明的固定输入形状做一次零输入探测，得到真实输出形状。

        RKNNLite 不提供输出形状查询；sidecar 缺少形状时退化为无形状描述。
        探测失败说明模型在当前运行时不可用，直接报错而不是带病加载。
        """
        if not self._input_sizes or any(size is None for size in self._input_sizes):
            return [_IONode(f"output_{i}") for i in range(output_count)]
        dummy = [np.zeros(size, dtype=np.float32) for size in self._input_sizes if size is not None]
        try:
            outputs = self._rknn.inference(inputs=dummy, data_format=["nchw"] * len(dummy))
        except Exception as exc:
            raise RknnUnavailableError(f"RKNN probe inference failed for {self.model_path}: {exc}") from exc
        if outputs is None:
            raise RknnUnavailableError(f"RKNN probe inference returned no outputs: {self.model_path}")
        return [_IONode(f"output_{i}", tuple(np.asarray(out).shape)) for i, out in enumerate(outputs)]

    @property
    def input_size(self) -> list[list[int] | None]:
        """sidecar 声明的固定输入形状（与输入顺序一致），缺失位置为 None。"""
        return list(self._input_sizes)

    def get_inputs(self) -> list[_IONode]:
        """返回输入节点描述，顺序即 RKNN 的位置输入顺序。"""
        return list(self._inputs)

    def get_outputs(self) -> list[_IONode]:
        """返回输出节点描述。"""
        return list(self._outputs)

    def run(self, output_names: list[str] | None, input_feed: dict[str, np.ndarray]) -> list[np.ndarray]:
        """按输入名展开为位置输入并推理；output_names 仅为接口兼容，RKNN 固定返回全部输出。"""
        if not input_feed:
            raise ValueError("RKNN input feed must not be empty")
        names = [node.name for node in self._inputs]
        if len(names) == 1:
            values = [next(iter(input_feed.values()))]
        elif all(name in input_feed for name in names):
            values = [input_feed[name] for name in names]
        else:
            logger.warning(
                "RKNN input names {} not fully present in feed {}; falling back to insertion order",
                names,
                list(input_feed),
            )
            values = list(input_feed.values())
        outputs = self._rknn.inference(inputs=values, data_format=["nchw"] * len(values))
        if outputs is None:
            raise RuntimeError(f"RKNN inference returned no outputs: {self.model_path}")
        return [np.asarray(output) for output in outputs]

    def release(self) -> None:
        """释放 NPU 运行时资源。"""
        self._rknn.release()


def rknn_session(model_path: str, *, core_mask: str | None = None) -> RknnSession:
    """创建 RKNN 会话；签名与 ort_session 对齐，device 维度由 RK3588 硬件本身决定。"""
    return RknnSession(model_path, core_mask=core_mask)
