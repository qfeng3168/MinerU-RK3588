# RKNN conversion — ocr_det (run 39372522458)

```json
{
  "model": "ocr_det",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "OCR/paddleocr/ch_PP-OCRv6_tiny_det_infer.onnx",
  "onnx_md5": "f00e81b2e940f0e8e709102883b45f63",
  "rknn_file": "ch_PP-OCRv6_tiny_det_rk3588.rknn",
  "rknn_md5": "43c0acbc1777acafa7ed645b5a0acc16",
  "rknn_bytes": 2682040,
  "input_names": [
    "x"
  ],
  "input_size": [
    [
      1,
      3,
      640,
      640
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      1,
      1,
      640,
      640
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "OCR/paddleocr/ch_PP-OCRv6_tiny_det_rk3588.rknn",
  "hf_config_path": "OCR/paddleocr/ch_PP-OCRv6_tiny_det_inference.yml",
  "config_md5": "b95b62f8c5c9c88fa999be42c01af308"
}```

## conversion log (tail)
```
D RKNN: [05:01:53.585] 96  ConvAdd         conv2d_161.w_0                                 FLOAT16   (160,320,1,1) | 0x0009e5c0 0x000b75c0 0x00019000
D RKNN: [05:01:53.585] 96  ConvAdd         _v_839                                         FLOAT     (160)         | 0x000d3880 0x000d3b00 0x00000280
D RKNN: [05:01:53.585] 97  Conv            conv2d_91.w_0                                  FLOAT16   (64,160,1,1)  | 0x000b75c0 0x000bc5c0 0x00005000
D RKNN: [05:01:53.585] 98  Conv            GlobalAveragePool.0_2conv0_i1                  FLOAT16   (1,64,7,7)    | 0x000d4640 0x000d5ec0 0x00001880
D RKNN: [05:01:53.585] 98  Conv            GlobalAveragePool.0_2conv0_i2                  FLOAT     (64)          | 0x000d5ec0 0x000d5fc0 0x00000100
D RKNN: [05:01:53.585] 99  Conv            GlobalAveragePool.0_2conv1_i1                  FLOAT16   (1,64,3,3)    | 0x000d5fc0 0x000d6440 0x00000480
D RKNN: [05:01:53.585] 99  Conv            GlobalAveragePool.0_2conv1_i2                  FLOAT     (64)          | 0x000d6440 0x000d6540 0x00000100
D RKNN: [05:01:53.585] 100 ConvRelu        conv2d_92.w_0                                  FLOAT16   (16,64,1,1)   | 0x000bc5c0 0x000bcdc0 0x00000800
D RKNN: [05:01:53.585] 100 ConvRelu        _v_842                                         FLOAT     (16)          | 0x000d3b00 0x000d3b40 0x00000040
D RKNN: [05:01:53.585] 101 ConvHardSigmoid conv2d_93.w_0                                  FLOAT16   (64,16,1,1)   | 0x000bcdc0 0x000bd5c0 0x00000800
D RKNN: [05:01:53.585] 101 ConvHardSigmoid _v_845                                         FLOAT     (64)          | 0x000d3b40 0x000d3c40 0x00000100
D RKNN: [05:01:53.585] 104 Conv            conv2d_165.w_0                                 FLOAT16   (1,64,5,5)    | 0x000c4e40 0x000c5ac0 0x00000c80
D RKNN: [05:01:53.585] 104 Conv            _v_866                                         FLOAT     (64)          | 0x000d4000 0x000d4100 0x00000100
D RKNN: [05:01:53.585] 105 Conv            conv2d_97.w_0                                  FLOAT16   (16,64,1,1)   | 0x000c5ac0 0x000c62c0 0x00000800
D RKNN: [05:01:53.585] 106 Conv            GlobalAveragePool.4_2conv0_i1                  FLOAT16   (1,16,7,7)    | 0x000d6540 0x000d6b60 0x00000620
D RKNN: [05:01:53.585] 106 Conv            GlobalAveragePool.4_2conv0_i2                  FLOAT     (16)          | 0x000d6b80 0x000d6c00 0x00000080
D RKNN: [05:01:53.585] 107 Conv            GlobalAveragePool.4_2conv1_i1                  FLOAT16   (1,16,3,3)    | 0x000d6c00 0x000d6d20 0x00000120
D RKNN: [05:01:53.585] 107 Conv            GlobalAveragePool.4_2conv1_i2                  FLOAT     (16)          | 0x000d6d40 0x000d6dc0 0x00000080
D RKNN: [05:01:53.585] 108 ConvRelu        conv2d_98.w_0                                  FLOAT16   (4,16,1,1)    | 0x000c62c0 0x000c6340 0x00000080
D RKNN: [05:01:53.585] 108 ConvRelu        _v_869                                         FLOAT     (4)           | 0x000d4100 0x000d4140 0x00000040
D RKNN: [05:01:53.585] 109 ConvHardSigmoid conv2d_99.w_0                                  FLOAT16   (16,4,1,1)    | 0x000c6340 0x000c6440 0x00000100
D RKNN: [05:01:53.585] 109 ConvHardSigmoid _v_872                                         FLOAT     (16)          | 0x000d4140 0x000d4180 0x00000040
D RKNN: [05:01:53.585] 112 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [05:01:53.585] 112 Resize          helper.constant.39                             FLOAT     (4)           | 0x000c4dc0 0x000c4e40 0x00000080
D RKNN: [05:01:53.585] 114 Conv            conv2d_164.w_0                                 FLOAT16   (1,64,5,5)    | 0x000c6440 0x000c70c0 0x00000c80
D RKNN: [05:01:53.585] 114 Conv            _v_875                                         FLOAT     (64)          | 0x000d4180 0x000d4280 0x00000100
D RKNN: [05:01:53.585] 115 Conv            conv2d_88.w_0                                  FLOAT16   (16,64,1,1)   | 0x000c70c0 0x000c78c0 0x00000800
D RKNN: [05:01:53.585] 116 Conv            GlobalAveragePool.5_2conv0_i1                  FLOAT16   (1,16,7,7)    | 0x000d9a40 0x000da060 0x00000620
D RKNN: [05:01:53.585] 116 Conv            GlobalAveragePool.5_2conv0_i2                  FLOAT     (16)          | 0x000da080 0x000da100 0x00000080
D RKNN: [05:01:53.585] 117 Conv            GlobalAveragePool.5_2conv1_i1                  FLOAT16   (1,16,6,6)    | 0x000da100 0x000da580 0x00000480
D RKNN: [05:01:53.585] 117 Conv            GlobalAveragePool.5_2conv1_i2                  FLOAT     (16)          | 0x000da580 0x000da600 0x00000080
D RKNN: [05:01:53.585] 118 ConvRelu        conv2d_89.w_0                                  FLOAT16   (4,16,1,1)    | 0x000c78c0 0x000c7940 0x00000080
D RKNN: [05:01:53.585] 118 ConvRelu        _v_878                                         FLOAT     (4)           | 0x000d4280 0x000d42c0 0x00000040
D RKNN: [05:01:53.585] 119 ConvHardSigmoid conv2d_90.w_0                                  FLOAT16   (16,4,1,1)    | 0x000c7940 0x000c7a40 0x00000100
D RKNN: [05:01:53.585] 119 ConvHardSigmoid _v_881                                         FLOAT     (16)          | 0x000d42c0 0x000d4300 0x00000040
D RKNN: [05:01:53.585] 122 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [05:01:53.585] 122 Resize          helper.constant.39                             FLOAT     (4)           | 0x000c4dc0 0x000c4e40 0x00000080
D RKNN: [05:01:53.585] 124 Conv            conv2d_163.w_0                                 FLOAT16   (1,64,5,5)    | 0x000c7a40 0x000c86c0 0x00000c80
D RKNN: [05:01:53.585] 124 Conv            _v_884                                         FLOAT     (64)          | 0x000d4300 0x000d4400 0x00000100
D RKNN: [05:01:53.585] 125 Conv            conv2d_79.w_0                                  FLOAT16   (16,64,1,1)   | 0x000c86c0 0x000c8ec0 0x00000800
D RKNN: [05:01:53.585] 126 Conv            GlobalAveragePool.6_2conv0_i1                  FLOAT16   (1,16,7,7)    | 0x000ddc00 0x000de220 0x00000620
D RKNN: [05:01:53.585] 126 Conv            GlobalAveragePool.6_2conv0_i2                  FLOAT     (16)          | 0x000de240 0x000de2c0 0x00000080
D RKNN: [05:01:53.585] 127 Conv            GlobalAveragePool.6_2conv1_i1                  FLOAT16   (1,16,7,7)    | 0x000de2c0 0x000de8e0 0x00000620
D RKNN: [05:01:53.585] 127 Conv            GlobalAveragePool.6_2conv1_i2                  FLOAT     (16)          | 0x000de900 0x000de980 0x00000080
D RKNN: [05:01:53.585] 128 Conv            GlobalAveragePool.6_2conv2_i1                  FLOAT16   (1,16,2,2)    | 0x000de980 0x000dea00 0x00000080
D RKNN: [05:01:53.585] 128 Conv            GlobalAveragePool.6_2conv2_i2                  FLOAT     (16)          | 0x000dea00 0x000dea80 0x00000080
D RKNN: [05:01:53.585] 129 ConvRelu        conv2d_80.w_0                                  FLOAT16   (4,16,1,1)    | 0x000c8ec0 0x000c8f40 0x00000080
D RKNN: [05:01:53.585] 129 ConvRelu        _v_887                                         FLOAT     (4)           | 0x000d4400 0x000d4440 0x00000040
D RKNN: [05:01:53.585] 130 ConvHardSigmoid conv2d_81.w_0                                  FLOAT16   (16,4,1,1)    | 0x000c8f40 0x000c9040 0x00000100
D RKNN: [05:01:53.585] 130 ConvHardSigmoid _v_890                                         FLOAT     (16)          | 0x000d4440 0x000d4480 0x00000040
D RKNN: [05:01:53.585] 133 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [05:01:53.585] 133 Resize          helper.constant.39                             FLOAT     (4)           | 0x000c4dc0 0x000c4e40 0x00000080
D RKNN: [05:01:53.585] 135 Conv            conv2d_162.w_0                                 FLOAT16   (1,64,5,5)    | 0x000c9040 0x000c9cc0 0x00000c80
D RKNN: [05:01:53.585] 135 Conv            _v_893                                         FLOAT     (64)          | 0x000d4480 0x000d4580 0x00000100
D RKNN: [05:01:53.585] 136 Conv            conv2d_70.w_0                                  FLOAT16   (16,64,1,1)   | 0x000c9cc0 0x000ca4c0 0x00000800
D RKNN: [05:01:53.585] 137 Conv            GlobalAveragePool.7_2conv0_i1                  FLOAT16   (1,16,7,7)    | 0x000e2680 0x000e2ca0 0x00000620
D RKNN: [05:01:53.585] 137 Conv            GlobalAveragePool.7_2conv0_i2                  FLOAT     (16)          | 0x000e2cc0 0x000e2d40 0x00000080
D RKNN: [05:01:53.585] 138 Conv            GlobalAveragePool.7_2conv1_i1                  FLOAT16   (1,16,7,7)    | 0x000e2d40 0x000e3360 0x00000620
D RKNN: [05:01:53.585] 138 Conv            GlobalAveragePool.7_2conv1_i2                  FLOAT     (16)          | 0x000e3380 0x000e3400 0x00000080
D RKNN: [05:01:53.585] 139 Conv            GlobalAveragePool.7_2conv2_i1                  FLOAT16   (1,16,4,4)    | 0x000e3400 0x000e3600 0x00000200
D RKNN: [05:01:53.585] 139 Conv            GlobalAveragePool.7_2conv2_i2                  FLOAT     (16)          | 0x000e3600 0x000e3680 0x00000080
D RKNN: [05:01:53.585] 140 ConvRelu        conv2d_71.w_0                                  FLOAT16   (4,16,1,1)    | 0x000ca4c0 0x000ca540 0x00000080
D RKNN: [05:01:53.585] 140 ConvRelu        _v_896                                         FLOAT     (4)           | 0x000d4580 0x000d45c0 0x00000040
D RKNN: [05:01:53.585] 141 ConvHardSigmoid conv2d_72.w_0                                  FLOAT16   (16,4,1,1)    | 0x000ca540 0x000ca640 0x00000100
D RKNN: [05:01:53.585] 141 ConvHardSigmoid _v_899                                         FLOAT     (16)          | 0x000d45c0 0x000d4600 0x00000040
D RKNN: [05:01:53.585] 144 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [05:01:53.585] 144 Resize          helper.constant.45                             FLOAT     (4)           | 0x000ca640 0x000ca6c0 0x00000080
D RKNN: [05:01:53.585] 145 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [05:01:53.585] 145 Resize          helper.constant.47                             FLOAT     (4)           | 0x000ca6c0 0x000ca740 0x00000080
D RKNN: [05:01:53.585] 146 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [05:01:53.585] 146 Resize          helper.constant.39                             FLOAT     (4)           | 0x000c4dc0 0x000c4e40 0x00000080
D RKNN: [05:01:53.585] 148 ConvRelu        conv2d_166.w_0                                 FLOAT16   (16,64,3,3)   | 0x000ca740 0x000cef40 0x00004800
D RKNN: [05:01:53.58I rknn building done.
I Target is None, use simulator!
I GraphPreparing :   0%|                                                    | 0/209 [00:00<?, ?it/s]I GraphPreparing : 100%|███████████████████████████████████████| 209/209 [00:00<00:00, 10279.31it/s]
I SessionPreparing :   0%|                                                  | 0/209 [00:00<?, ?it/s]I SessionPreparing : 100%|██████████████████████████████████████| 209/209 [00:00<00:00, 3050.40it/s]
{
  "model": "ocr_det",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "OCR/paddleocr/ch_PP-OCRv6_tiny_det_infer.onnx",
  "onnx_md5": "f00e81b2e940f0e8e709102883b45f63",
  "rknn_file": "ch_PP-OCRv6_tiny_det_rk3588.rknn",
  "rknn_md5": "43c0acbc1777acafa7ed645b5a0acc16",
  "rknn_bytes": 2682040,
  "input_names": [
    "x"
  ],
  "input_size": [
    [
      1,
      3,
      640,
      640
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      1,
      1,
      640,
      640
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "OCR/paddleocr/ch_PP-OCRv6_tiny_det_rk3588.rknn",
  "hf_config_path": "OCR/paddleocr/ch_PP-OCRv6_tiny_det_inference.yml",
  "config_md5": "b95b62f8c5c9c88fa999be42c01af308"
}
5] 148 ConvRelu        _v_902                                         FLOAT     (16)          | 0x000d4600 0x000d4640 0x00000040
D RKNN: [05:01:53.585] 149 ConvTranspose   auto.cast.95                                   FLOAT16   (16,16,2,2)   | 0x000cef40 0x000cf740 0x00000800
D RKNN: [05:01:53.585] 150 AddRelu         p2o.pd_op.reshape.75.0                         FLOAT     (1,16,1,1)    | 0x000cf740 0x000cf780 0x00000040
D RKNN: [05:01:53.585] 151 ConvTranspose   auto.cast.98                                   FLOAT16   (16,1,2,2)    | 0x000cf780 0x000cf800 0x00000080
D RKNN: [05:01:53.585] 152 Add             p2o.pd_op.reshape.76.0                         FLOAT     (1,1,1,1)     | 0x000cf800 0x000cf840 0x00000040
D RKNN: [05:01:53.585] -------------------------------------------------------------------------------------------+---------------------------------
D RKNN: [05:01:53.585] ----------------------------------------
D RKNN: [05:01:53.585] Total Internal Memory Size: 20000KB
D RKNN: [05:01:53.585] Total Weight Memory Size: 971.125KB
D RKNN: [05:01:53.585] ----------------------------------------
D RKNN: [05:01:53.585] <<<<<<<< end: rknn::RKNNMemStatisticsPass
```
