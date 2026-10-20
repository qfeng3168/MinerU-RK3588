# Copyright (c) Opendatalab. All rights reserved.
"""小模型后端会话工厂：按 ``small_backend`` 选用 onnxruntime 或 RKNN 会话。

消费者的模型加载只经过这两个入口，不需要知道后端的具体会话类型；
所有返回的会话都实现 ``get_inputs()`` / ``get_outputs()`` / ``run(None, feed)``。
"""

from __future__ import annotations

from typing import Any

from .device import resolve_small_model_backend
from .onnx import ort_session, table_ort_session

__all__ = ["small_model_session", "table_small_model_session"]


def small_model_session(
    small_backend: str | None,
    model_path: str,
    *,
    device: str | None = None,
    intra_op_num_threads: int = 0,
) -> Any:
    """通用小模型会话：onnx 走 onnxruntime CPU，rknn 走 RK3588 NPU。"""
    if resolve_small_model_backend(small_backend) == "rknn":
        from .rknn import RknnSession

        return RknnSession(model_path)
    return ort_session(model_path, device, intra_op_num_threads)


def table_small_model_session(
    small_backend: str | None,
    model_path: str,
    *,
    sess_options: Any = None,
) -> Any:
    """表格模型会话：沿用表格专用设备与回退策略；rknn 时走 NPU 会话。"""
    if resolve_small_model_backend(small_backend) == "rknn":
        from .rknn import RknnSession

        return RknnSession(model_path)
    return table_ort_session(model_path, sess_options=sess_options)
