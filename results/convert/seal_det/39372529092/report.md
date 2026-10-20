# RKNN conversion — seal_det (run 39372529092)

```json
{
  "model": "seal_det",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "OCR/paddleocr/seal_PP-OCRv4_det_infer.onnx",
  "onnx_md5": "1addbf19efba72db4ec7bb3d2ce77a70",
  "rknn_file": "seal_PP-OCRv4_det_rk3588.rknn",
  "rknn_md5": "8a5413a5ea81d05acd91b0e4274832c6",
  "rknn_bytes": 4151796,
  "input_names": [
    "image"
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
  "hf_rknn_path": "OCR/paddleocr/seal_PP-OCRv4_det_rk3588.rknn",
  "hf_config_path": "OCR/paddleocr/seal_PP-OCRv4_det_inference.yml",
  "config_md5": "e0d088e6e5bb96d326e16de4278a6006"
}```

## conversion log (tail)
```
D RKNN: [05:01:36.253] 114 ConvHardSwish        backbone.blocks6.3.pw_conv.reparam_conv.bias                        FLOAT     (384)         | 0x001a46c0 0x001a4cc0 0x00000600
D RKNN: [05:01:36.253] 115 Mul                  backbone.blocks6.3.pw_conv.act.lab.scale                            FLOAT     (1,1,1,1)     | 0x0015c640 0x0015c680 0x00000040
D RKNN: [05:01:36.253] 116 Add                  backbone.blocks6.3.pw_conv.act.lab.bias                             FLOAT     (1,1,1,1)     | 0x0015c680 0x0015c6c0 0x00000040
D RKNN: [05:01:36.253] 117 Conv                 backbone.layer_list.3.weight                                        FLOAT16   (360,384,1,1) | 0x001a9f40 0x001ed740 0x00043800
D RKNN: [05:01:36.253] 117 Conv                 backbone.layer_list.3.bias                                          FLOAT     (360)         | 0x001ed740 0x001edd00 0x000005c0
D RKNN: [05:01:36.253] 118 Conv                 neck.ins_conv.3.in_conv.weight                                      FLOAT16   (96,360,1,1)  | 0x001fa900 0x0020b700 0x00010e00
D RKNN: [05:01:36.253] 119 Conv                 /neck/ins_conv.3/se_block/avg_pool/GlobalAveragePool_2conv0_i1      FLOAT16   (1,96,7,7)    | 0x00255980 0x00257e40 0x000024c0
D RKNN: [05:01:36.253] 119 Conv                 /neck/ins_conv.3/se_block/avg_pool/GlobalAveragePool_2conv0_i2      FLOAT     (96)          | 0x00257e40 0x00257fc0 0x00000180
D RKNN: [05:01:36.253] 120 Conv                 /neck/ins_conv.3/se_block/avg_pool/GlobalAveragePool_2conv1_i1      FLOAT16   (1,96,3,3)    | 0x00257fc0 0x00258680 0x000006c0
D RKNN: [05:01:36.253] 120 Conv                 /neck/ins_conv.3/se_block/avg_pool/GlobalAveragePool_2conv1_i2      FLOAT     (96)          | 0x00258680 0x00258800 0x00000180
D RKNN: [05:01:36.253] 121 ConvRelu             neck.ins_conv.3.se_block.conv1.weight                               FLOAT16   (24,96,1,1)   | 0x0020b700 0x0020c900 0x00001200
D RKNN: [05:01:36.253] 121 ConvRelu             neck.ins_conv.3.se_block.conv1.bias                                 FLOAT     (24)          | 0x0020c900 0x0020c980 0x00000080
D RKNN: [05:01:36.253] 122 ConvClip             neck.ins_conv.3.se_block.conv2.weight                               FLOAT16   (96,24,1,1)   | 0x0020c980 0x0020e180 0x00001800
D RKNN: [05:01:36.253] 122 ConvClip             neck.ins_conv.3.se_block.conv2.bias                                 FLOAT     (96)          | 0x0020e180 0x0020e300 0x00000180
D RKNN: [05:01:36.253] 123 Mul                  /neck/ins_conv.3/se_block/hard_sigmoid/act/Div_2mul_i1              FLOAT     (1,1,1,1)     | 0x00258800 0x00258840 0x00000040
D RKNN: [05:01:36.253] 126 Conv                 neck.inp_conv.3.in_conv.weight                                      FLOAT16   (24,96,3,3)   | 0x0022d440 0x00237640 0x0000a200
D RKNN: [05:01:36.253] 127 Conv                 /neck/inp_conv.3/se_block/avg_pool/GlobalAveragePool_2conv0_i1      FLOAT16   (1,24,7,7)    | 0x00258840 0x00259480 0x00000c40
D RKNN: [05:01:36.253] 127 Conv                 /neck/inp_conv.3/se_block/avg_pool/GlobalAveragePool_2conv0_i2      FLOAT     (24)          | 0x00259480 0x00259500 0x00000080
D RKNN: [05:01:36.253] 128 Conv                 /neck/inp_conv.3/se_block/avg_pool/GlobalAveragePool_2conv1_i1      FLOAT16   (1,24,3,3)    | 0x00259500 0x00259740 0x00000240
D RKNN: [05:01:36.253] 128 Conv                 /neck/inp_conv.3/se_block/avg_pool/GlobalAveragePool_2conv1_i2      FLOAT     (24)          | 0x00259740 0x002597c0 0x00000080
D RKNN: [05:01:36.253] 129 ConvRelu             neck.inp_conv.3.se_block.conv1.weight                               FLOAT16   (6,24,1,1)    | 0x00237640 0x002377c0 0x00000180
D RKNN: [05:01:36.253] 129 ConvRelu             neck.inp_conv.3.se_block.conv1.bias                                 FLOAT     (6)           | 0x002377c0 0x00237800 0x00000040
D RKNN: [05:01:36.253] 130 ConvClip             neck.inp_conv.3.se_block.conv2.weight                               FLOAT16   (24,6,1,1)    | 0x00237800 0x00237980 0x00000180
D RKNN: [05:01:36.253] 130 ConvClip             neck.inp_conv.3.se_block.conv2.bias                                 FLOAT     (24)          | 0x00237980 0x00237a00 0x00000080
D RKNN: [05:01:36.253] 131 Mul                  /neck/inp_conv.3/se_block/hard_sigmoid/act/Div_2mul_i1              FLOAT     (1,1,1,1)     | 0x002597c0 0x00259800 0x00000040
D RKNN: [05:01:36.253] 134 Resize               empty_placeholder_0                                                 FLOAT     (1)           | 0x0026d680 0x0026d700 0x00000080
D RKNN: [05:01:36.253] 134 Resize               /neck/Constant_output_0                                             FLOAT     (4)           | 0x00243f80 0x00244000 0x00000080
D RKNN: [05:01:36.253] 136 Conv                 neck.inp_conv.2.in_conv.weight                                      FLOAT16   (24,96,3,3)   | 0x00222e80 0x0022d080 0x0000a200
D RKNN: [05:01:36.253] 137 Conv                 /neck/inp_conv.2/se_block/avg_pool/GlobalAveragePool_2conv0_i1      FLOAT16   (1,24,7,7)    | 0x0025db00 0x0025e740 0x00000c40
D RKNN: [05:01:36.253] 137 Conv                 /neck/inp_conv.2/se_block/avg_pool/GlobalAveragePool_2conv0_i2      FLOAT     (24)          | 0x0025e740 0x0025e7c0 0x00000080
D RKNN: [05:01:36.253] 138 Conv                 /neck/inp_conv.2/se_block/avg_pool/GlobalAveragePool_2conv1_i1      FLOAT16   (1,24,6,6)    | 0x0025e7c0 0x0025f0c0 0x00000900
D RKNN: [05:01:36.253] 138 Conv                 /neck/inp_conv.2/se_block/avg_pool/GlobalAveragePool_2conv1_i2      FLOAT     (24)          | 0x0025f0c0 0x0025f140 0x00000080
D RKNN: [05:01:36.253] 139 ConvRelu             neck.inp_conv.2.se_block.conv1.weight                               FLOAT16   (6,24,1,1)    | 0x0022d080 0x0022d200 0x00000180
D RKNN: [05:01:36.253] 139 ConvRelu             neck.inp_conv.2.se_block.conv1.bias                                 FLOAT     (6)           | 0x0022d200 0x0022d240 0x00000040
D RKNN: [05:01:36.253] 140 ConvClip             neck.inp_conv.2.se_block.conv2.weight                               FLOAT16   (24,6,1,1)    | 0x0022d240 0x0022d3c0 0x00000180
D RKNN: [05:01:36.253] 140 ConvClip             neck.inp_conv.2.se_block.conv2.bias                                 FLOAT     (24)          | 0x0022d3c0 0x0022d440 0x00000080
D RKNN: [05:01:36.253] 141 Mul                  /neck/inp_conv.2/se_block/hard_sigmoid/act/Div_2mul_i1              FLOAT     (1,1,1,1)     | 0x0025f140 0x0025f180 0x00000040
D RKNN: [05:01:36.253] 144 Resize               empty_placeholder_0                                                 FLOAT     (1)           | 0x0026d680 0x0026d700 0x00000080
D RKNN: [05:01:36.253] 144 Resize               /neck/Constant_1_output_0                                           FLOAT     (4)           | 0x00244000 0x00244080 0x00000080
D RKNN: [05:01:36.253] 146 Conv                 neck.inp_conv.1.in_conv.weight                                      FLOAT16   (24,96,3,3)   | 0x002188c0 0x00222ac0 0x0000a200
D RKNN: [05:01:36.253] 147 Conv                 /neck/inp_conv.1/se_block/avg_pool/GlobalAveragePool_2conv0_i1      FLOAT16   (1,24,7,7)    | 0x002642c0 0x00264f00 0x00000c40
D RKNN: [05:01:36.253] 147 Conv                 /neck/inp_conv.1/se_block/avg_pool/GlobalAveragePool_2conv0_i2      FLOAT     (24)          | 0x00264f00 0x00264f80 0x00000080
D RKNN: [05:01:36.253] 148 Conv                 /neck/inp_conv.1/se_block/avg_pool/GlobalAveragePool_2conv1_i1      FLOAT16   (1,24,7,7)    | 0x00264f80 0x00265bc0 0x00000c40
D RKNN: [05:01:36.253] 148 Conv                 /neck/inp_conv.1/se_block/avg_pool/GlobalAveragePool_2conv1_i2      FLOAT     (24)          | 0x00265bc0 0x00265c40 0x00000080
D RKNN: [05:01:36.253] 149 Conv                 /neck/inp_conv.1/se_block/avg_pool/GlobalAveragePool_2conv2_i1      FLOAT16   (1,24,2,2)    | 0x00265c40 0x00265d40 0x00000100
D RKNN: [05:01:36.253] 149 Conv                 /neck/inp_conv.1/se_block/avg_pool/GlobalAveragePool_2conv2_i2      FLOAT     (24)          | 0x00265d40 0x00265dc0 0x00000080
D RKNN: [05:01:36.253] 150 ConvRelu             neck.inp_conv.1.se_block.conv1.weight                               FLOAT16   (6,24,1,1)    | 0x00222ac0 0x00222c40 0x00000180
D RKNN: [05:01:36.253] 150 ConvRelu             neck.inp_conv.1.se_block.conv1.bias                                 FLOAT     (6)           | 0x00222c40 0x00222c80 0x00000040
D RKNN: [05:01:36.253] 151 ConvClip             neck.inp_conv.1.se_block.conv2.weight                               FLOAT16   (24,6,1,1)    | 0x00222c80 0x00222e00 0x00000180
D RKNN: [05:01:36.253] 151 ConvClip             neck.inp_conv.1.se_block.conv2.bias                                 FLOAT     (24)          | 0x00222e00 0x00222e80 0x00000080
D RKNN: [05:01:36.253] 152 Mul                  /neck/inp_conv.1/se_block/hard_sigmoid/act/Div_2mul_i1              FLOAT     (1,1,1,1)     | 0x00265dc0 0x00265e00 0x00000040
D RKNN: [05:01:36.253] 155 Resize               empty_placeholder_0                                                 FLOAT     (1)           | 0x0026d680 0x0026d700 0x00000080
D RKNN: [05:01:36.253] 155 Resize               /neck/Constant_2_output_0                                           FLOAT     (4)           | 0x00244080 0x00244100 0x00000080
D RKNN: [05:01:36.253] 157 Conv                 neck.inp_conv.0.in_conv.weight                                      FLOAT16   (24,96,3,3)   | 0x0020e300 0x00218500 0x0000a200
D RKNN: [05:01:36.253] 158 Conv                 /neck/inp_conv.0/se_block/avg_pool/GlobalAveragePool_2conv0_i1      FLOAT16   (1,24,7,7)    | 0x0026b840 0x0026c480 0x00000c40
D RKNN: [05:01:36.253] 158 Conv                 /neck/inp_conv.0/se_block/avg_pool/GlobalAveragePool_2conv0_i2      FLOAT     (24)          | 0x0026c480 0x0026c500 0x00000080
D RKNN: [05:01:36.253] 159 Conv                 /neck/inp_conv.0/se_block/avg_pool/GlobalAveragePool_2conv1_i1      FLOAT16   (1,24,7,7)    | 0x0026c500 0x0026d140 0x00000c40
D RKNN: [05:01:36.253] 159 Conv                 /neck/inp_conv.0/se_block/avg_pool/GlobalAveragePool_2conv1_i2      FLOAT     (24)          | 0x0026d140 0x0026d1c0 0x00000080
D RKNN: [05:01:36.253] 160 Conv                 /neck/inp_conv.0/se_block/avg_pool/GlobalAveragePool_2conv2_i1      FLOAT16   (1,24,4,4)    | 0x0026d1c0 0x0026d5c0 0x00000400
D RKNN: [05:01:36.253] 160 Conv                 /neck/inp_conv.0/se_block/avg_pool/GlobalAveragePool_2conv2_i2      FLOAT     (24)          | 0x0026d5c0 0x0026d640 0x00000080
D RKNN: [05:01:36.253] 161 ConvRelu             neck.inp_conv.0.se_block.conv1.weight                               FLOAT16   (6,24,1,1)    | 0x00218500 0x00218680 0x00000180
D RKNN: [05:01:36.253] 161 ConvRelu             neck.inp_conv.0.se_block.conv1.bias                                 FLOAT     (6)           | 0x00218680 0x002186c0 0x00000040
D RKNN: [05:01:36.253] 162 ConvClip             neck.inp_conv.0.se_block.conv2.weight                               FLOAT16   (24,6,1,1)    | 0x002186c0 0x00218840 0x00000180
D RKNN: [05:01:36.253] 162 ConvClip             neck.inp_conv.0.se_block.conv2.bias                                 FLOAT     (24)          | 0x00218840 0x002188c0 0x00000080
D RKNN: [05:01:36.253] 163 Mul                  /neck/inp_conv.0/se_block/hard_sigmoid/act/Div_2mul_i1              FLOAT     (1,1,1,1)     | 0x0026d640 0x0026d680 0x00000040
D RKNN: [05:01:36.253] 166 Resize               empty_placehI rknn building done.
I Target is None, use simulator!
I GraphPreparing :   0%|                                                    | 0/219 [00:00<?, ?it/s]I GraphPreparing : 100%|███████████████████████████████████████| 219/219 [00:00<00:00, 10563.30it/s]
I SessionPreparing :   0%|                                                  | 0/219 [00:00<?, ?it/s]I SessionPreparing : 100%|██████████████████████████████████████| 219/219 [00:00<00:00, 2780.09it/s]
{
  "model": "seal_det",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "OCR/paddleocr/seal_PP-OCRv4_det_infer.onnx",
  "onnx_md5": "1addbf19efba72db4ec7bb3d2ce77a70",
  "rknn_file": "seal_PP-OCRv4_det_rk3588.rknn",
  "rknn_md5": "8a5413a5ea81d05acd91b0e4274832c6",
  "rknn_bytes": 4151796,
  "input_names": [
    "image"
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
  "hf_rknn_path": "OCR/paddleocr/seal_PP-OCRv4_det_rk3588.rknn",
  "hf_config_path": "OCR/paddleocr/seal_PP-OCRv4_det_inference.yml",
  "config_md5": "e0d088e6e5bb96d326e16de4278a6006"
}
older_0                                                 FLOAT     (1)           | 0x0026d680 0x0026d700 0x00000080
D RKNN: [05:01:36.253] 166 Resize               /neck/Constant_3_output_0                                           FLOAT     (4)           | 0x00244100 0x00244180 0x00000080
D RKNN: [05:01:36.253] 167 Resize               empty_placeholder_0                                                 FLOAT     (1)           | 0x0026d680 0x0026d700 0x00000080
D RKNN: [05:01:36.253] 167 Resize               /neck/Constant_4_output_0                                           FLOAT     (4)           | 0x00244180 0x00244200 0x00000080
D RKNN: [05:01:36.253] 168 Resize               empty_placeholder_0                                                 FLOAT     (1)           | 0x0026d680 0x0026d700 0x00000080
D RKNN: [05:01:36.253] 168 Resize               /neck/Constant_5_output_0                                           FLOAT     (4)           | 0x00244200 0x00244280 0x00000080
D RKNN: [05:01:36.253] 170 ConvRelu             onnx::Conv_1476                                                     FLOAT16   (24,96,3,3)   | 0x00239d00 0x00243f00 0x0000a200
D RKNN: [05:01:36.253] 170 ConvRelu             onnx::Conv_1477                                                     FLOAT     (24)          | 0x00243f00 0x00243f80 0x00000080
D RKNN: [05:01:36.253] 171 ConvTransposeRelu    head.binarize.conv2.weight                                          FLOAT16   (24,24,2,2)   | 0x00237a00 0x00239200 0x00001800
D RKNN: [05:01:36.253] 171 ConvTransposeRelu    head.binarize.conv2.bias                                            FLOAT     (24)          | 0x00239200 0x00239280 0x00000080
D RKNN: [05:01:36.253] 172 ConvTransposeSigmoid head.binarize.conv3.weight                                          FLOAT16   (24,1,2,2)    | 0x00239280 0x00239380 0x00000100
D RKNN: [05:01:36.253] 172 ConvTransposeSigmoid head.binarize.conv3.bias                                            FLOAT     (1)           | 0x00239380 0x002393c0 0x00000040
D RKNN: [05:01:36.253] ---------------------------------------------------------------------------------------------------------------------+---------------------------------
D RKNN: [05:01:36.253] ----------------------------------------
D RKNN: [05:01:36.253] Total Internal Memory Size: 33600KB
D RKNN: [05:01:36.253] Total Weight Memory Size: 2487.75KB
D RKNN: [05:01:36.253] ----------------------------------------
D RKNN: [05:01:36.253] <<<<<<<< end: rknn::RKNNMemStatisticsPass
```
