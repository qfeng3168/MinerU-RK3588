# RKNN conversion — ocr_rec (run 39372526074)

```json
{
  "model": "ocr_rec",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "OCR/paddleocr/ch_PP-OCRv6_small_rec_infer.onnx",
  "onnx_md5": "9a31d8e2576ef51d8d24f8879a814832",
  "rknn_file": "ch_PP-OCRv6_small_rec_rk3588.rknn",
  "rknn_md5": "0704fb6838cd135c31608d3f7e65fb36",
  "rknn_bytes": 12544758,
  "input_names": [
    "x"
  ],
  "input_size": [
    [
      1,
      3,
      48,
      320
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      1,
      40,
      18710
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "OCR/paddleocr/ch_PP-OCRv6_small_rec_rk3588.rknn",
  "hf_config_path": "OCR/paddleocr/ch_PP-OCRv6_small_rec_inference.yml",
  "config_md5": "2d55410ba3e9a1244b4fcb6241e40afd"
}```

## conversion log (tail)
```
D RKNN: [05:01:58.851] 57  ConvExGelu      p2o.pd_op.conv2d.29.0_bias           FLOAT     (384)           | 0x00a66c00 0x00a67200 0x00000600
D RKNN: [05:01:58.851] 58  ConvAdd         conv2d_107.w_0                       FLOAT16   (192,384,1,1)   | 0x001d5f80 0x001f9f80 0x00024000
D RKNN: [05:01:58.851] 58  ConvAdd         p2o.pd_op.conv2d.30.0_bias           FLOAT     (192)           | 0x00a67200 0x00a67500 0x00000300
D RKNN: [05:01:58.851] 59  Conv            conv2d_109.w_0                       FLOAT16   (1,192,3,3)     | 0x001f9f80 0x001fad00 0x00000d80
D RKNN: [05:01:58.851] 59  Conv            p2o.pd_op.depthwise_conv2d.9.0_bias  FLOAT     (192)           | 0x00a67500 0x00a67800 0x00000300
D RKNN: [05:01:58.851] 60  ConvExGelu      conv2d_110.w_0                       FLOAT16   (384,192,1,1)   | 0x001fad00 0x0021ed00 0x00024000
D RKNN: [05:01:58.851] 60  ConvExGelu      p2o.pd_op.conv2d.31.0_bias           FLOAT     (384)           | 0x00a67800 0x00a67e00 0x00000600
D RKNN: [05:01:58.851] 61  ConvAdd         conv2d_111.w_0                       FLOAT16   (192,384,1,1)   | 0x0021ed00 0x00242d00 0x00024000
D RKNN: [05:01:58.851] 61  ConvAdd         p2o.pd_op.conv2d.32.0_bias           FLOAT     (192)           | 0x00a67e00 0x00a68100 0x00000300
D RKNN: [05:01:58.851] 62  Conv            conv2d_112.w_0                       FLOAT16   (1,192,3,3)     | 0x00242d00 0x00243a80 0x00000d80
D RKNN: [05:01:58.851] 62  Conv            p2o.pd_op.depthwise_conv2d.10.0_bias FLOAT     (192)           | 0x00a68100 0x00a68400 0x00000300
D RKNN: [05:01:58.851] 63  ConvExGelu      conv2d_113.w_0                       FLOAT16   (384,192,1,1)   | 0x00243a80 0x00267a80 0x00024000
D RKNN: [05:01:58.851] 63  ConvExGelu      p2o.pd_op.conv2d.33.0_bias           FLOAT     (384)           | 0x00a68400 0x00a68a00 0x00000600
D RKNN: [05:01:58.851] 64  Conv            conv2d_114.w_0                       FLOAT16   (384,384,1,1)   | 0x00267a80 0x002afa80 0x00048000
D RKNN: [05:01:58.851] 64  Conv            p2o.pd_op.conv2d.34.0_bias           FLOAT     (384)           | 0x00a68a00 0x00a69000 0x00000600
D RKNN: [05:01:58.851] 65  Conv            conv2d_116.w_0                       FLOAT16   (1,384,3,3)     | 0x002afa80 0x002b1580 0x00001b00
D RKNN: [05:01:58.851] 65  Conv            p2o.pd_op.depthwise_conv2d.11.0_bias FLOAT     (384)           | 0x00a69000 0x00a69600 0x00000600
D RKNN: [05:01:58.851] 66  Conv            p2o.pd_op.add.55.0_gavg_2conv0_i1    FLOAT16   (1,384,3,7)     | 0x00a803c0 0x00a842c0 0x00003f00
D RKNN: [05:01:58.851] 66  Conv            p2o.pd_op.add.55.0_gavg_2conv0_i2    FLOAT     (384)           | 0x00a842c0 0x00a848c0 0x00000600
D RKNN: [05:01:58.851] 67  Conv            p2o.pd_op.add.55.0_gavg_2conv1_i1    FLOAT16   (1,384,1,7)     | 0x00a848c0 0x00a85dc0 0x00001500
D RKNN: [05:01:58.851] 67  Conv            p2o.pd_op.add.55.0_gavg_2conv1_i2    FLOAT     (384)           | 0x00a85dc0 0x00a863c0 0x00000600
D RKNN: [05:01:58.851] 68  Conv            p2o.pd_op.add.55.0_gavg_2conv2_i1    FLOAT16   (1,384,1,2)     | 0x00a863c0 0x00a869c0 0x00000600
D RKNN: [05:01:58.851] 68  Conv            p2o.pd_op.add.55.0_gavg_2conv2_i2    FLOAT     (384)           | 0x00a869c0 0x00a86fc0 0x00000600
D RKNN: [05:01:58.851] 69  ConvRelu        conv2d_57.w_0                        FLOAT16   (96,384,1,1)    | 0x002b1580 0x002c3580 0x00012000
D RKNN: [05:01:58.851] 69  ConvRelu        p2o.pd_op.conv2d.35.0_bias           FLOAT     (96)            | 0x00a69600 0x00a69780 0x00000180
D RKNN: [05:01:58.851] 70  ConvHardSigmoid conv2d_58.w_0                        FLOAT16   (384,96,1,1)    | 0x002c3580 0x002d5580 0x00012000
D RKNN: [05:01:58.851] 70  ConvHardSigmoid p2o.pd_op.conv2d.36.0_bias           FLOAT     (384)           | 0x00a69780 0x00a69d80 0x00000600
D RKNN: [05:01:58.851] 72  ConvExGelu      conv2d_117.w_0                       FLOAT16   (768,384,1,1)   | 0x002d5580 0x00365580 0x00090000
D RKNN: [05:01:58.851] 72  ConvExGelu      p2o.pd_op.conv2d.37.0_bias           FLOAT     (768)           | 0x00a69d80 0x00a6a980 0x00000c00
D RKNN: [05:01:58.851] 73  ConvAdd         conv2d_118.w_0                       FLOAT16   (384,768,1,1)   | 0x00365580 0x003f5580 0x00090000
D RKNN: [05:01:58.851] 73  ConvAdd         p2o.pd_op.conv2d.38.0_bias           FLOAT     (384)           | 0x00a6a980 0x00a6af80 0x00000600
D RKNN: [05:01:58.851] 74  Conv            conv2d_120.w_0                       FLOAT16   (1,384,3,3)     | 0x003f5580 0x003f7080 0x00001b00
D RKNN: [05:01:58.851] 74  Conv            p2o.pd_op.depthwise_conv2d.12.0_bias FLOAT     (384)           | 0x00a6af80 0x00a6b580 0x00000600
D RKNN: [05:01:58.851] 75  ConvExGelu      conv2d_121.w_0                       FLOAT16   (768,384,1,1)   | 0x003f7080 0x00487080 0x00090000
D RKNN: [05:01:58.851] 75  ConvExGelu      p2o.pd_op.conv2d.39.0_bias           FLOAT     (768)           | 0x00a6b580 0x00a6c180 0x00000c00
D RKNN: [05:01:58.851] 76  ConvAdd         conv2d_122.w_0                       FLOAT16   (384,768,1,1)   | 0x00487080 0x00517080 0x00090000
D RKNN: [05:01:58.851] 76  ConvAdd         p2o.pd_op.conv2d.40.0_bias           FLOAT     (384)           | 0x00a6c180 0x00a6c780 0x00000600
D RKNN: [05:01:58.851] 78  ConvExSwish     conv2d_67.w_0                        FLOAT16   (120,384,1,1)   | 0x00517080 0x0052d880 0x00016800
D RKNN: [05:01:58.851] 78  ConvExSwish     batch_norm2d_57.b_0_306_bias         FLOAT     (120)           | 0x00a6c780 0x00a6c980 0x00000200
D RKNN: [05:01:58.851] 79  ConvExSwish     conv2d_65.w_0                        FLOAT16   (120,384,1,1)   | 0x0052d880 0x00544080 0x00016800
D RKNN: [05:01:58.851] 79  ConvExSwish     batch_norm2d_55.b_0_310_bias         FLOAT     (120)           | 0x00a6c980 0x00a6cb80 0x00000200
D RKNN: [05:01:58.851] 80  ConvExSwish     conv2d_66.w_0                        FLOAT16   (1,120,1,7)     | 0x00544080 0x00544780 0x00000700
D RKNN: [05:01:58.851] 80  ConvExSwish     batch_norm2d_56.b_0_314_bias         FLOAT     (120)           | 0x00a6cb80 0x00a6cd80 0x00000200
D RKNN: [05:01:58.851] 82  exNorm          helper.reshape.0                     FLOAT16   (1,120,1,1)     | 0x00544780 0x00544880 0x00000100
D RKNN: [05:01:58.851] 82  exNorm          helper.reshape.1                     FLOAT     (1,120,1,1)     | 0x00544880 0x00544a80 0x00000200
D RKNN: [05:01:58.851] 83  Conv            linear_0.w_0                         FLOAT16   (360,120,1,1)   | 0x00544a80 0x0055b280 0x00016800
D RKNN: [05:01:58.851] 83  Conv            linear_0.b_0                         FLOAT     (360)           | 0x0055b280 0x0055b840 0x000005c0
D RKNN: [05:01:58.851] 84  Reshape         Transpose.1#1_i1                     INT64     (4)             | 0x00a87080 0x00a870a0 0x00000020
D RKNN: [05:01:58.851] 85  Split           Slice.4_2sp_split                    INT64     (3)             | 0x00a6cd80 0x00a6cd98 0x00000018
D RKNN: [05:01:58.851] 87  Reshape         p2o.pd_op.reshape.55.0_rs_i1_sw      INT64     (4)             | 0x00a87000 0x00a87020 0x00000020
D RKNN: [05:01:58.851] 88  ConvAdd         linear_1.w_0                         FLOAT16   (120,120,1,1)   | 0x0055b840 0x00563040 0x00007800
D RKNN: [05:01:58.851] 88  ConvAdd         linear_1.b_0                         FLOAT     (120)           | 0x00563040 0x00563240 0x00000200
D RKNN: [05:01:58.851] 89  exNorm          helper.reshape.2                     FLOAT16   (1,120,1,1)     | 0x00563240 0x00563340 0x00000100
D RKNN: [05:01:58.851] 89  exNorm          helper.reshape.3                     FLOAT     (1,120,1,1)     | 0x00563340 0x00563540 0x00000200
D RKNN: [05:01:58.851] 90  ConvExSwish     linear_2.w_0                         FLOAT16   (240,120,1,1)   | 0x00563540 0x00572540 0x0000f000
D RKNN: [05:01:58.851] 90  ConvExSwish     linear_2.b_0                         FLOAT     (240)           | 0x00572540 0x00572900 0x000003c0
D RKNN: [05:01:58.851] 91  ConvAdd         linear_3.w_0                         FLOAT16   (120,240,1,1)   | 0x00572900 0x00580a00 0x0000e100
D RKNN: [05:01:58.851] 91  ConvAdd         linear_3.b_0                         FLOAT     (120)           | 0x00580a00 0x00580c00 0x00000200
D RKNN: [05:01:58.851] 92  exNorm          helper.reshape.4                     FLOAT16   (1,120,1,1)     | 0x00580c00 0x00580d00 0x00000100
D RKNN: [05:01:58.851] 92  exNorm          helper.reshape.5                     FLOAT     (1,120,1,1)     | 0x00580d00 0x00580f00 0x00000200
D RKNN: [05:01:58.851] 93  Conv            linear_4.w_0                         FLOAT16   (360,120,1,1)   | 0x00580f00 0x00597700 0x00016800
D RKNN: [05:01:58.851] 93  Conv            linear_4.b_0                         FLOAT     (360)           | 0x00597700 0x00597cc0 0x000005c0
D RKNN: [05:01:58.851] 94  Reshape         Transpose.4#1_i1                     INT64     (4)             | 0x00a870c0 0x00a870e0 0x00000020
D RKNN: [05:01:58.851] 95  Split           Slice.12_2sp_split                   INT64     (3)             | 0x00a6cdc0 0x00a6cdd8 0x00000018
D RKNN: [05:01:58.851] 97  Reshape         p2o.pd_op.reshape.57.0_rs_i1_sw      INT64     (4)             | 0x00a87040 0x00a87060 0x00000020
D RKNN: [05:01:58.851] 98  ConvAdd         linear_5.w_0                         FLOAT16   (120,120,1,1)   | 0x00597cc0 0x0059f4c0 0x00007800
D RKNN: [05:01:58.851] 98  ConvAdd         linear_5.b_0                         FLOAT     (120)           | 0x0059f4c0 0x0059f6c0 0x00000200
D RKNN: [05:01:58.851] 99  exNorm          helper.reshape.6                     FLOAT16   (1,120,1,1)     | 0x0059f6c0 0x0059f7c0 0x00000100
D RKNN: [05:01:58.851] 99  exNorm          helper.reshape.7                     FLOAT     (1,120,1,1)     | 0x0059f7c0 0x0059f9c0 0x00000200
D RKNN: [05:01:58.851] 100 ConvExSwish     linear_6.w_0                         FLOAT16   (240,120,1,1)   | 0x0059f9c0 0x005ae9c0 0x0000f000
D RKNN: [05:01:58.851] 100 ConvExSwish     linear_6.b_0                         FLOAT     (240)           | 0x005ae9c0 0x005aed80 0x000003c0
D RKNN: [05:01:58.851] 101 ConvAdd         linear_7.w_0                         FLOAT16   (120,240,1,1)   | 0x005aed80 0x005bce80 0x0000e100
D RKNN: [05:01:58.851] 101 ConvAdd         linear_7.b_0                         FLOAT     (120)           | 0x005bce80 0x005bd080 0x00000200
D RKNN: [05:01:58.851] 102 exNorm          helper.reshape.8                     FLOAT16   (1,120,1,1)     | 0x005bd080 0x005bd180 0x00000100
D RKNN: [05:01:58.851] 102 exNorm          helper.reshape.9                     FLOAT     (1,120I rknn building done.
I Target is None, use simulator!
I GraphPreparing :   0%|                                                    | 0/155 [00:00<?, ?it/s]I GraphPreparing : 100%|███████████████████████████████████████| 155/155 [00:00<00:00, 11896.67it/s]
I SessionPreparing :   0%|                                                  | 0/155 [00:00<?, ?it/s]I SessionPreparing : 100%|██████████████████████████████████████| 155/155 [00:00<00:00, 3056.54it/s]
{
  "model": "ocr_rec",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "OCR/paddleocr/ch_PP-OCRv6_small_rec_infer.onnx",
  "onnx_md5": "9a31d8e2576ef51d8d24f8879a814832",
  "rknn_file": "ch_PP-OCRv6_small_rec_rk3588.rknn",
  "rknn_md5": "0704fb6838cd135c31608d3f7e65fb36",
  "rknn_bytes": 12544758,
  "input_names": [
    "x"
  ],
  "input_size": [
    [
      1,
      3,
      48,
      320
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      1,
      40,
      18710
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "OCR/paddleocr/ch_PP-OCRv6_small_rec_rk3588.rknn",
  "hf_config_path": "OCR/paddleocr/ch_PP-OCRv6_small_rec_inference.yml",
  "config_md5": "2d55410ba3e9a1244b4fcb6241e40afd"
}
,1,1)     | 0x005bd180 0x005bd380 0x00000200
D RKNN: [05:01:58.851] 104 Conv            linear_8.w_0                         FLOAT16   (18710,120,1,1) | 0x005bd380 0x00a4e980 0x00491600
D RKNN: [05:01:58.851] 104 Conv            linear_8.b_0                         FLOAT     (18710)         | 0x00a4e980 0x00a60e00 0x00012480
D RKNN: [05:01:58.851] 107 Reshape         fetch_name_0-rs_i1                   INT64     (3)             | 0x00a86fc0 0x00a86fd8 0x00000018
D RKNN: [05:01:58.851] -----------------------------------------------------------------------------------+---------------------------------
D RKNN: [05:01:58.851] ----------------------------------------
D RKNN: [05:01:58.851] Total Internal Memory Size: 10274.4KB
D RKNN: [05:01:58.851] Total Weight Memory Size: 10782.2KB
D RKNN: [05:01:58.851] ----------------------------------------
D RKNN: [05:01:58.851] <<<<<<<< end: rknn::RKNNMemStatisticsPass
```
