from __future__ import annotations

import json
import sys
import types
from pathlib import Path

import numpy as np
import pytest

from mineru.model.registry import MINERU_RK3588_MODELS, MODEL_REPOS_BY_NAME, small_model_repo
from mineru.model.runtime import device
from mineru.model.runtime.rknn import RknnUnavailableError, rknn_available, rknn_session

_PIPELINE_KEYS = (
    "pp_doclayout_v2",
    "ocr_det",
    "ocr_rec",
    "seal_det",
    "pp_formulanet_plus_m_weights",
    "slanet_plus",
    "unet_structure",
    "paddle_table_cls",
)


def test_rk3588_repo_registered() -> None:
    """RK3588 仓库注册进总表，具名路径覆盖 pipeline 全部小模型与 VLM 产物。"""
    assert MODEL_REPOS_BY_NAME["MinerU-4_models_rknn"] is MINERU_RK3588_MODELS
    assert small_model_repo("rknn") is MINERU_RK3588_MODELS
    for key in _PIPELINE_KEYS:
        assert key in MINERU_RK3588_MODELS.paths, key
    assert MINERU_RK3588_MODELS.paths["pp_doclayout_v2"].endswith(".rknn")
    assert MINERU_RK3588_MODELS.paths["vlm_llm"].endswith(".rkllm")
    assert MINERU_RK3588_MODELS.paths["vlm_vision"].endswith(".rknn")


def test_resolve_small_model_backend_rknn(monkeypatch: pytest.MonkeyPatch) -> None:
    """显式 rknn 直接命中；auto 在 rk3588 设备下自动选择 rknn。"""
    assert device.resolve_small_model_backend("rknn") == "rknn"
    monkeypatch.setattr(device, "get_device", lambda: "rk3588")
    monkeypatch.setattr(device, "module_available", lambda name: name == "rknnlite")
    assert device.resolve_small_model_backend("auto") == "rknn"
    with pytest.raises(ValueError, match="Unsupported small backend"):
        device.resolve_small_model_backend("npu")


def test_rknn_unavailable_without_rknnlite(monkeypatch: pytest.MonkeyPatch) -> None:
    """无 rknnlite 时明确报不可用，而不是静默回退或导入错误。"""
    monkeypatch.setattr(device, "module_available", lambda name: False)
    assert rknn_available() is False
    with pytest.raises(RknnUnavailableError):
        rknn_session("/nonexistent/model.rknn")


class _FakeLite:
    """最小 RKNNLite 桩：记录推理入参，返回固定两路输出。"""

    NPU_CORE_AUTO = 0
    NPU_CORE_0 = 1
    NPU_CORE_1 = 2
    NPU_CORE_2 = 3
    NPU_CORE_0_1_2 = 4

    def __init__(self) -> None:
        self.inference_calls: list[list[np.ndarray]] = []

    def load_rknn(self, path: str) -> int:
        return 0

    def init_runtime(self, core_mask: int = 0) -> int:
        return 0

    def inference(self, inputs: list[np.ndarray]) -> list[np.ndarray]:
        self.inference_calls.append(inputs)
        return [np.zeros((1, 8), dtype=np.float32), np.zeros((1,), dtype=np.int64)]

    def release(self) -> None:
        return None


def test_rknn_session_feed_mapping(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """多输入按 sidecar 声明顺序展开 feed，与 onnxruntime 的 dict 喂入行为等价。"""
    model = tmp_path / "layout_rk3588.rknn"
    model.write_bytes(b"fake")
    (tmp_path / (model.name + ".inputs.json")).write_text(json.dumps(["image", "scale_factor"]), encoding="utf-8")

    fake_api = types.ModuleType("rknnlite.api")
    fake_api.RKNNLite = _FakeLite  # type: ignore[attr-defined]
    fake_package = types.ModuleType("rknnlite")
    fake_package.api = fake_api  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "rknnlite", fake_package)
    monkeypatch.setitem(sys.modules, "rknnlite.api", fake_api)
    monkeypatch.setattr(device, "module_available", lambda name: name == "rknnlite")

    session = rknn_session(str(model))
    assert [node.name for node in session.get_inputs()] == ["image", "scale_factor"]
    image = np.zeros((1, 3, 800, 800), dtype=np.float32)
    scale = np.ones((1, 2), dtype=np.float32)
    outputs = session.run(None, {"scale_factor": scale, "image": image})
    assert len(outputs) == 2
    assert outputs[0].shape == (1, 8)
    lite = session._rknn  # noqa: SLF001 - 验证桩的实际入参顺序
    assert lite.inference_calls[0][0] is image
    assert lite.inference_calls[0][1] is scale
    session.release()
