#!/usr/bin/env python3
# Copyright (c) Opendatalab. All rights reserved.
"""MinerU 小模型 ONNX -> RKNN 转换（在 x86 CI 上运行，产物分发给 RK3588 板）。

用法:
    python tools/rk3588/convert.py ocr_det --out-dir build/rknn

- 输入 ONNX 直接从上游 HF 仓库 opendatalab/MinerU-4_models_onnx 按 registry
  路径下载，保证出处可追溯；不使用任何本地来历不明的文件。
- 第一阶段只做 fp 转换（do_quantization=False），先保证数值与 ONNX 基线一致；
  INT8 量化在验收门通过后单独引入，需要校准集，不在此脚本内隐含。
- 产物除 .rknn 本体外，还写出 <model>.rknn.inputs.json（运行时输入顺序清单）
  与 report.json（版本、md5、形状自检结果）。
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

ONNX_REPO_ID = "opendatalab/MinerU-4_models_onnx"
HF_REPO_ID = "q81801/MinerU-RK3588-models"


@dataclass(frozen=True)
class ModelSpec:
    """单个模型的转换规格：上游 ONNX 相对路径、固定输入形状、产物与 HF 目标路径。"""

    onnx_path: str
    input_size: list[list[int]]
    output_name: str
    hf_rknn_path: str
    onnx_config_path: str | None = None
    hf_config_path: str | None = None


MODEL_SPECS: dict[str, ModelSpec] = {
    "ocr_det": ModelSpec(
        onnx_path="OCR/paddleocr/ch_PP-OCRv6_tiny_det_infer.onnx",
        input_size=[[1, 3, 640, 640]],
        output_name="ch_PP-OCRv6_tiny_det_rk3588.rknn",
        hf_rknn_path="OCR/paddleocr/ch_PP-OCRv6_tiny_det_rk3588.rknn",
        onnx_config_path="OCR/paddleocr/ch_PP-OCRv6_tiny_det_inference.yml",
        hf_config_path="OCR/paddleocr/ch_PP-OCRv6_tiny_det_inference.yml",
    ),
    "ocr_rec": ModelSpec(
        onnx_path="OCR/paddleocr/ch_PP-OCRv6_small_rec_infer.onnx",
        input_size=[[1, 3, 48, 320]],
        output_name="ch_PP-OCRv6_small_rec_rk3588.rknn",
        hf_rknn_path="OCR/paddleocr/ch_PP-OCRv6_small_rec_rk3588.rknn",
        onnx_config_path="OCR/paddleocr/ch_PP-OCRv6_small_rec_inference.yml",
        hf_config_path="OCR/paddleocr/ch_PP-OCRv6_small_rec_inference.yml",
    ),
    "seal_det": ModelSpec(
        onnx_path="OCR/paddleocr/seal_PP-OCRv4_det_infer.onnx",
        input_size=[[1, 3, 640, 640]],
        output_name="seal_PP-OCRv4_det_rk3588.rknn",
        hf_rknn_path="OCR/paddleocr/seal_PP-OCRv4_det_rk3588.rknn",
        onnx_config_path="OCR/paddleocr/seal_PP-OCRv4_det_inference.yml",
        hf_config_path="OCR/paddleocr/seal_PP-OCRv4_det_inference.yml",
    ),
    "pp_doclayout_v2": ModelSpec(
        onnx_path="Layout/PP-DocLayoutV2/inference.onnx",
        input_size=[[1, 3, 800, 800]],
        output_name="PP-DocLayoutV2_rk3588.rknn",
        hf_rknn_path="Layout/PP-DocLayoutV2_rk3588.rknn",
        onnx_config_path="Layout/PP-DocLayoutV2/inference.yml",
        hf_config_path="Layout/PP-DocLayoutV2/inference.yml",
    ),
    "pp_formulanet_plus_m": ModelSpec(
        onnx_path="MFR/pp_formulanet_plus_m/PP-FormulaNet_plus-M.onnx",
        input_size=[[1, 3, 384, 384]],
        output_name="PP-FormulaNet_plus-M_rk3588.rknn",
        hf_rknn_path="MFR/pp_formulanet_plus_m/PP-FormulaNet_plus-M_rk3588.rknn",
        onnx_config_path="MFR/pp_formulanet_plus_m/PP-FormulaNet_plus-M_inference.yml",
        hf_config_path="MFR/pp_formulanet_plus_m/PP-FormulaNet_plus-M_inference.yml",
    ),
    "slanet_plus": ModelSpec(
        onnx_path="Table/slanet-plus.onnx",
        input_size=[[1, 3, 488, 488]],
        output_name="slanet-plus_rk3588.rknn",
        hf_rknn_path="Table/slanet-plus_rk3588.rknn",
    ),
    "unet_structure": ModelSpec(
        onnx_path="Table/unet.onnx",
        input_size=[[1, 3, 768, 768]],
        output_name="unet_rk3588.rknn",
        hf_rknn_path="Table/unet_rk3588.rknn",
    ),
    "paddle_table_cls": ModelSpec(
        onnx_path="Table/PP-LCNet_x1_0_table_cls.onnx",
        input_size=[[1, 3, 224, 224]],
        output_name="PP-LCNet_x1_0_table_cls_rk3588.rknn",
        hf_rknn_path="Table/PP-LCNet_x1_0_table_cls_rk3588.rknn",
    ),
}


def _md5(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download_onnx(spec: ModelSpec, cache_dir: Path) -> Path:
    """从上游 HF 仓库下载原始 ONNX（自动下载机制与产品运行时共用同一出处）。"""
    from huggingface_hub import hf_hub_download

    local = hf_hub_download(repo_id=ONNX_REPO_ID, filename=spec.onnx_path, local_dir=str(cache_dir))
    return Path(local)


def convert(key: str, spec: ModelSpec, onnx_path: Path, cache_dir: Path, out_dir: Path) -> dict[str, object]:
    """执行一次转换并做模拟器自检，返回可 JSON 序列化的转换报告。"""
    import numpy as np
    import onnx
    from rknn.api import RKNN

    graph = onnx.load(str(onnx_path))
    input_names = [node.name for node in graph.graph.input if node.name not in {w.name for w in graph.graph.initializer}]

    rknn = RKNN(verbose=True)
    try:
        rknn.config(target_platform="rk3588")
        if rknn.load_onnx(model=str(onnx_path), inputs=input_names, input_size_list=spec.input_size) != 0:
            raise RuntimeError(f"load_onnx failed for {key}")
        if rknn.build(do_quantization=False) != 0:
            raise RuntimeError(f"build failed for {key}")
        out_path = out_dir / spec.output_name
        out_path.parent.mkdir(parents=True, exist_ok=True)
        if rknn.export_rknn(str(out_path)) != 0:
            raise RuntimeError(f"export_rknn failed for {key}")
        if rknn.init_runtime() != 0:
            raise RuntimeError(f"init_runtime (simulator) failed for {key}")
        dummy = [np.zeros(size, dtype=np.float32) for size in spec.input_size]
        outputs = rknn.inference(inputs=dummy, data_format=["nchw"] * len(dummy))
        if outputs is None:
            raise RuntimeError(f"simulator inference returned nothing for {key}")
        output_shapes = [list(out.shape) for out in outputs]
    finally:
        rknn.release()

    sidecar = out_dir / (spec.output_name + ".inputs.json")
    sidecar.write_text(
        json.dumps({"input_names": input_names, "input_size": spec.input_size}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    config_md5: str | None = None
    if spec.onnx_config_path and spec.hf_config_path:
        from huggingface_hub import hf_hub_download

        config_local = Path(
            hf_hub_download(repo_id=ONNX_REPO_ID, filename=spec.onnx_config_path, local_dir=str(cache_dir))
        )
        config_target = out_dir / Path(spec.hf_config_path).name
        config_target.write_bytes(config_local.read_bytes())
        config_md5 = _md5(config_target)

    return {
        "model": key,
        "onnx_repo": ONNX_REPO_ID,
        "onnx_path": spec.onnx_path,
        "onnx_md5": _md5(onnx_path),
        "rknn_file": spec.output_name,
        "rknn_md5": _md5(out_path),
        "rknn_bytes": out_path.stat().st_size,
        "input_names": input_names,
        "input_size": spec.input_size,
        "quantization": "none (fp)",
        "selfcheck_output_shapes": output_shapes,
        "hf_repo": HF_REPO_ID,
        "hf_rknn_path": spec.hf_rknn_path,
        "hf_config_path": spec.hf_config_path,
        "config_md5": config_md5,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert a MinerU ONNX small model to RKNN (rk3588).")
    parser.add_argument("model", choices=sorted(MODEL_SPECS), help="Registry model key to convert.")
    parser.add_argument("--out-dir", default="build/rknn", help="Output directory for .rknn + sidecar + report.")
    parser.add_argument("--cache-dir", default="build/onnx-cache", help="Download cache for upstream ONNX files.")
    args = parser.parse_args()

    spec = MODEL_SPECS[args.model]
    out_dir = Path(args.out_dir)
    cache_dir = Path(args.cache_dir)
    onnx_path = download_onnx(spec, cache_dir)
    report = convert(args.model, spec, onnx_path, cache_dir, out_dir)
    (out_dir / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
