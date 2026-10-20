# RKNN conversion — pp_doclayout_v2 (run 39374688155)

```json
{
  "model": "pp_doclayout_v2",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "Layout/PP-DocLayoutV2/inference.onnx",
  "onnx_md5": "19394e89733be3ce9a44abbd120232d1",
  "rknn_file": "PP-DocLayoutV2_rk3588.rknn",
  "rknn_md5": "9ef677b413ee04ad970c6dc50f5b463d",
  "rknn_bytes": 139740540,
  "input_names": [
    "im_shape",
    "image",
    "scale_factor"
  ],
  "input_size": [
    [
      1,
      2
    ],
    [
      1,
      3,
      800,
      800
    ],
    [
      1,
      2
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      300,
      8
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "Layout/PP-DocLayoutV2_rk3588.rknn",
  "hf_config_path": "Layout/PP-DocLayoutV2/inference.yml",
  "config_md5": "936cdd9b873cee5e28f194ca4b68c43e"
}```

## conversion log (tail)
```
D RKNN: [05:26:34.646] 900 Slice              p2o.pd_op.full_int_array.401.0              INT64     (1)             | 0x06701280 0x06701288 0x00000008
D RKNN: [05:26:34.646] 900 Slice              p2o.pd_op.full_int_array.402.0              INT64     (1)             | 0x067012c0 0x067012c8 0x00000008
D RKNN: [05:26:34.646] 900 Slice              helper.constant.1390                        INT64     (1)             | 0x06701300 0x06701308 0x00000008
D RKNN: [05:26:34.646] 900 Slice              helper.constant.1389                        INT64     (1)             | 0x06701340 0x06701348 0x00000008
D RKNN: [05:26:34.646] 901 Conv               linear_95.w_0_deepcopy_906                  FLOAT16   (128,512,1,1)   | 0x06701380 0x06721380 0x00020000
D RKNN: [05:26:34.646] 901 Conv               linear_95.b_0_deepcopy_907                  FLOAT     (128)           | 0x06721380 0x06721580 0x00000200
D RKNN: [05:26:34.646] 902 Reshape            p2o.pd_op.reshape.124.0_rs_rs_i1_sw         INT64     (4)             | 0x07b15d40 0x07b15d60 0x00000020
D RKNN: [05:26:34.646] 903 Split              Slice.278_2sp_split                         INT64     (2)             | 0x07adfc40 0x07adfc50 0x00000010
D RKNN: [05:26:34.646] 904 exMatMul           auto.cast.914                               FLOAT     (1,1,1,1)       | 0x06721580 0x067215c0 0x00000040
D RKNN: [05:26:34.646] 906 Add                Sub.30_2add_i1                              FLOAT16   (1,300,1,300)   | 0x07ae0300 0x07b0cb80 0x0002c880
D RKNN: [05:26:34.646] 908 Mul                p2o.pd_op.triu.0.0                          FLOAT16   (1,300,1,300)   | 0x067216c0 0x0674df40 0x0002c880
D RKNN: [05:26:34.646] 910 BatchNormalization Mul.309_2bn_i1                              FLOAT16   (300)           | 0x07b0cb80 0x07b0cde0 0x00000260
D RKNN: [05:26:34.646] 910 BatchNormalization Mul.309_2bn_i2                              FLOAT     (300)           | 0x07b0ce00 0x07b0d2c0 0x000004c0
D RKNN: [05:26:34.646] 910 BatchNormalization Mul.309_2bn_i3                              FLOAT     (300)           | 0x07b0d2c0 0x07b0d780 0x000004c0
D RKNN: [05:26:34.646] 910 BatchNormalization Mul.309_2bn_i4                              FLOAT16   (300)           | 0x07b0d780 0x07b0d9e0 0x00000260
D RKNN: [05:26:34.646] 911 Mul                p2o.pd_op.tril.1.0                          FLOAT16   (1,300,1,300)   | 0x0674df40 0x0677a7c0 0x0002c880
D RKNN: [05:26:34.646] 913 Conv               ReduceSum.14_2conv_i1                       FLOAT16   (1,300,1,1)     | 0x07b15440 0x07b156a0 0x00000260
D RKNN: [05:26:34.646] 914 TopK               helper.slice.49                             INT64     (1)             | 0x0677a7c0 0x0677a7c8 0x00000008
D RKNN: [05:26:34.646] 915 Concat             Unsqueeze.422                               INT64     (1,1,1,300)     | 0x07abba80 0x07abc3e0 0x00000960
D RKNN: [05:26:34.646] 917 Reshape            Concat.246-rs_i1                            INT64     (3)             | 0x07b0da40 0x07b0da58 0x00000018
D RKNN: [05:26:34.646] 918 ScatterND          p2o.pd_op.full_with_tensor.5.0              INT64     (1,300)         | 0x07abc400 0x07abcd60 0x00000960
D RKNN: [05:26:34.646] 918 ScatterND          Expand.40                                   INT64     (1,300)         | 0x07abcd80 0x07abd6e0 0x00000960
D RKNN: [05:26:34.646] 920 Reshape            p2o.pd_op.unsqueeze.50.0_rs_i1              INT64     (4)             | 0x07b156c0 0x07b156e0 0x00000020
D RKNN: [05:26:34.646] 922 Reshape            ReduceSum.15-rs_iI rknn building done.
I Target is None, use simulator!
I GraphPreparing :   0%|                                                   | 0/1069 [00:00<?, ?it/s]I GraphPreparing :  50%|███████████████████▎                   | 531/1069 [00:00<00:00, 5309.57it/s]I GraphPreparing : 100%|██████████████████████████████████████| 1069/1069 [00:00<00:00, 6845.43it/s]
I SessionPreparing :   0%|                                                 | 0/1069 [00:00<?, ?it/s]I SessionPreparing :  14%|█████▏                               | 150/1069 [00:00<00:00, 1084.75it/s]I SessionPreparing :  31%|███████████▌                         | 334/1069 [00:00<00:00, 1467.84it/s]I SessionPreparing :  52%|███████████████████▍                 | 561/1069 [00:00<00:00, 1799.94it/s]I SessionPreparing :  74%|███████████████████████████▌         | 796/1069 [00:00<00:00, 1994.36it/s]I SessionPreparing :  94%|█████████████████████████████████▋  | 1000/1069 [00:00<00:00, 1545.39it/s]I SessionPreparing : 100%|████████████████████████████████████| 1069/1069 [00:00<00:00, 1411.16it/s]
[1;33mW[0m [1;33minference: The range [-5.695024490356445, inf] of 'p2o.pd_op.log.0.0-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.5791015625, inf] of 'Add.143-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.577934741973877, inf] of 'p2o.pd_op.log.1.0-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.4541778564453125, inf] of 'Add.207-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.452890396118164, inf] of 'p2o.pd_op.log.2.0-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.734375, inf] of 'Add.271-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.733768463134766, inf] of 'p2o.pd_op.log.3.0-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.756195068359375, inf] of 'Add.335-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.758240222930908, inf] of 'p2o.pd_op.log.4.0-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.4794921875, inf] of 'Add.399-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.4808831214904785, inf] of 'p2o.pd_op.log.5.0-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-5.484247207641602, inf] of 'Add.463-rs' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-13.802318572998047, inf] of 'auto.cast.713' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [1.0, inf] of 'p2o.pd_op.scale.72.0' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [0.0, inf] of 'auto.cast.712' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-13.8046875, inf] of 'p2o.pd_op.concat.16.0' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [0.0, inf] of 'Slice.216' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [0.0, inf] of 'Slice.218' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-13.8046875, inf] of 'Slice.220' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-13.8046875, inf] of 'Slice.222' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [0.0, inf] of 'p2o.pd_op.divide.8.0' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [0.0, inf] of 'p2o.pd_op.divide.9.0' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-1380.46875, inf] of 'p2o.pd_op.divide.10.0' is out of the float16![0m
[1;33mW[0m [1;33minference: The range [-1380.46875, inf] of 'p2o.pd_op.divide.11.0' is out of the float16![0m
{
  "model": "pp_doclayout_v2",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "Layout/PP-DocLayoutV2/inference.onnx",
  "onnx_md5": "19394e89733be3ce9a44abbd120232d1",
  "rknn_file": "PP-DocLayoutV2_rk3588.rknn",
  "rknn_md5": "9ef677b413ee04ad970c6dc50f5b463d",
  "rknn_bytes": 139740540,
  "input_names": [
    "im_shape",
    "image",
    "scale_factor"
  ],
  "input_size": [
    [
      1,
      2
    ],
    [
      1,
      3,
      800,
      800
    ],
    [
      1,
      2
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      300,
      8
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "Layout/PP-DocLayoutV2_rk3588.rknn",
  "hf_config_path": "Layout/PP-DocLayoutV2/inference.yml",
  "config_md5": "936cdd9b873cee5e28f194ca4b68c43e"
}
1                          INT64     (2)             | 0x07b0da00 0x07b0da10 0x00000010
D RKNN: [05:26:34.646] 924 Reshape            auto.cast.968_rs_i1                         INT64     (4)             | 0x07b0dd40 0x07b0dd60 0x00000020
D RKNN: [05:26:34.646] 926 Reshape            auto.cast.970                               INT64     (2)             | 0x0677a880 0x0677a890 0x00000010
D RKNN: [05:26:34.646] ---------------------------------------------------------------------------------------------+---------------------------------
D RKNN: [05:26:34.650] ----------------------------------------
D RKNN: [05:26:34.650] Total Internal Memory Size: 86466.6KB
D RKNN: [05:26:34.650] Total Weight Memory Size: 126064KB
D RKNN: [05:26:34.650] ----------------------------------------
D RKNN: [05:26:34.650] <<<<<<<< end: rknn::RKNNMemStatisticsPass
No lowering found for: GridSample.0, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.2, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.4, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.6, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.8, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.10, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.12, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.14, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.16, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.18, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.20, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.22, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.24, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.26, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.28, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.30, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.32, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: GridSample.34, node type = GridSample, use CustomOperatorLower instead.
No lowering found for: CumSum.0, node type = CumSum, use CustomOperatorLower instead.
```
