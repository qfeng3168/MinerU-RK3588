# RKNN conversion — paddle_table_cls (run 39372544801)

```json
{
  "model": "paddle_table_cls",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "Table/PP-LCNet_x1_0_table_cls.onnx",
  "onnx_md5": "83de43256e77c8cb5ac8eb57fecfbfe6",
  "rknn_file": "PP-LCNet_x1_0_table_cls_rk3588.rknn",
  "rknn_md5": "79583553c83de64b3d86a2a68d5ef90c",
  "rknn_bytes": 3956400,
  "input_names": [
    "x"
  ],
  "input_size": [
    [
      1,
      3,
      224,
      224
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      1,
      2
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "Table/PP-LCNet_x1_0_table_cls_rk3588.rknn",
  "hf_config_path": null,
  "config_md5": null
}```

## conversion log (tail)
```
D RKNN: [05:02:32.801] 41  OutputOperator  fetch_name_0                           FLOAT16   UNDEFINED    (1,2)          (1,2)           | 0x00000040 0x00000080 0x00000040
D RKNN: [05:02:32.801] -----------------------------------------------------------------------------------------------------------------+---------------------------------
D RKNN: [05:02:32.801] -------------------------------------------------------------------------------------------------------------------------
D RKNN: [05:02:32.801]                                         Const Tensor Information Table                              
D RKNN: [05:02:32.801] ---------------------------------------------------------------------------------------+---------------------------------
D RKNN: [05:02:32.801] ID  User            Tensor                                    DataType  OrigShape      |     [Start       End)       Size
D RKNN: [05:02:32.801] ---------------------------------------------------------------------------------------+---------------------------------
D RKNN: [05:02:32.801] 1   ConvHardSwish   conv2d_0.w_0_deepcopy_0                   FLOAT16   (16,3,3,3)     | 0x00000000 0x00000900 0x00000900
D RKNN: [05:02:32.801] 1   ConvHardSwish   batch_norm2d_0.b_0_deepcopy_2_1_bias      FLOAT     (16)           | 0x0032bfc0 0x0032c000 0x00000040
D RKNN: [05:02:32.801] 2   ConvHardSwish   conv2d_1.w_0_deepcopy_5                   FLOAT16   (1,16,3,3)     | 0x00000900 0x00000a20 0x00000120
D RKNN: [05:02:32.801] 2   ConvHardSwish   batch_norm2d_1.b_0_deepcopy_7_5_bias      FLOAT     (16)           | 0x0032c000 0x0032c080 0x00000080
D RKNN: [05:02:32.801] 3   ConvHardSwish   conv2d_2.w_0_deepcopy_10                  FLOAT16   (32,16,1,1)    | 0x00000a40 0x00000e40 0x00000400
D RKNN: [05:02:32.801] 3   ConvHardSwish   batch_norm2d_2.b_0_deepcopy_12_9_bias     FLOAT     (32)           | 0x0032c080 0x0032c100 0x00000080
D RKNN: [05:02:32.801] 4   ConvHardSwish   conv2d_3.w_0_deepcopy_15                  FLOAT16   (1,32,3,3)     | 0x00000e40 0x00001080 0x00000240
D RKNN: [05:02:32.801] 4   ConvHardSwish   batch_norm2d_3.b_0_deepcopy_17_13_bias    FLOAT     (32)           | 0x0032c100 0x0032c180 0x00000080
D RKNN: [05:02:32.801] 5   ConvHardSwish   conv2d_4.w_0_deepcopy_20                  FLOAT16   (64,32,1,1)    | 0x00001080 0x00002080 0x00001000
D RKNN: [05:02:32.801] 5   ConvHardSwish   batch_norm2d_4.b_0_deepcopy_22_17_bias    FLOAT     (64)           | 0x0032c180 0x0032c280 0x00000100
D RKNN: [05:02:32.801] 6   ConvHardSwish   conv2d_5.w_0_deepcopy_25                  FLOAT16   (1,64,3,3)     | 0x00002080 0x00002500 0x00000480
D RKNN: [05:02:32.801] 6   ConvHardSwish   batch_norm2d_5.b_0_deepcopy_27_21_bias    FLOAT     (64)           | 0x0032c280 0x0032c380 0x00000100
D RKNN: [05:02:32.801] 7   ConvHardSwish   conv2d_6.w_0_deepcopy_30                  FLOAT16   (64,64,1,1)    | 0x00002500 0x00004500 0x00002000
D RKNN: [05:02:32.801] 7   ConvHardSwish   batch_norm2d_6.b_0_deepcopy_32_25_bias    FLOAT     (64)           | 0x0032c380 0x0032c480 0x00000100
D RKNN: [05:02:32.801] 8   ConvHardSwish   conv2d_7.w_0_deepcopy_35                  FLOAT16   (1,64,3,3)     | 0x00004500 0x00004980 0x00000480
D RKNN: [05:02:32.801] 8   ConvHardSwish   batch_norm2d_7.b_0_deepcopy_37_29_bias    FLOAT     (64)           | 0x0032c480 0x0032c580 0x00000100
D RKNN: [05:02:32.801] 9   ConvHardSwish   conv2d_8.w_0_deepcopy_40                  FLOAT16   (128,64,1,1)   | 0x00004980 0x00008980 0x00004000
D RKNN: [05:02:32.801] 9   ConvHardSwish   batch_norm2d_8.b_0_deepcopy_42_33_bias    FLOAT     (128)          | 0x0032c580 0x0032c780 0x00000200
D RKNN: [05:02:32.801] 10  ConvHardSwish   conv2d_9.w_0_deepcopy_45                  FLOAT16   (1,128,3,3)    | 0x00008980 0x00009280 0x00000900
D RKNN: [05:02:32.801] 10  ConvHardSwish   batch_norm2d_9.b_0_deepcopy_47_37_bias    FLOAT     (128)          | 0x0032c780 0x0032c980 0x00000200
D RKNN: [05:02:32.801] 11  ConvHardSwish   conv2d_10.w_0_deepcopy_50                 FLOAT16   (128,128,1,1)  | 0x00009280 0x00011280 0x00008000
D RKNN: [05:02:32.801] 11  ConvHardSwish   batch_norm2d_10.b_0_deepcopy_52_41_bias   FLOAT     (128)          | 0x0032c980 0x0032cb80 0x00000200
D RKNN: [05:02:32.801] 12  ConvHardSwish   conv2d_11.w_0_deepcopy_55                 FLOAT16   (1,128,3,3)    | 0x00011280 0x00011b80 0x00000900
D RKNN: [05:02:32.801] 12  ConvHardSwish   batch_norm2d_11.b_0_deepcopy_57_45_bias   FLOAT     (128)          | 0x0032cb80 0x0032cd80 0x00000200
D RKNN: [05:02:32.801] 13  ConvHardSwish   conv2d_12.w_0_deepcopy_60                 FLOAT16   (256,128,1,1)  | 0x00011b80 0x00021b80 0x00010000
D RKNN: [05:02:32.801] 13  ConvHardSwish   batch_norm2d_12.b_0_deepcopy_62_49_bias   FLOAT     (256)          | 0x0032cd80 0x0032d180 0x00000400
D RKNN: [05:02:32.801] 14  ConvHardSwish   conv2d_13.w_0_deepcopy_65                 FLOAT16   (1,256,5,5)    | 0x00021b80 0x00024d80 0x00003200
D RKNN: [05:02:32.801] 14  ConvHardSwish   batch_norm2d_13.b_0_deepcopy_67_53_bias   FLOAT     (256)          | 0x0032d180 0x0032d580 0x00000400
D RKNN: [05:02:32.801] 15  ConvHardSwish   conv2d_14.w_0_deepcopy_70                 FLOAT16   (256,256,1,1)  | 0x00024d80 0x00044d80 0x00020000
D RKNN: [05:02:32.801] 15  ConvHardSwish   batch_norm2d_14.b_0_deepcopy_72_57_bias   FLOAT     (256)          | 0x0032d580 0x0032d980 0x00000400
D RKNN: [05:02:32.801] 16  ConvHardSwish   conv2d_15.w_0_deepcopy_75                 FLOAT16   (1,256,5,5)    | 0x00044d80 0x00047f80 0x00003200
D RKNN: [05:02:32.801] 16  ConvHardSwish   batch_norm2d_15.b_0_deepcopy_77_61_bias   FLOAT     (256)          | 0x0032d980 0x0032dd80 0x00000400
D RKNN: [05:02:32.801] 17  ConvHardSwish   conv2d_16.w_0_deepcopy_80                 FLOAT16   (256,256,1,1)  | 0x00047f80 0x00067f80 0x00020000
D RKNN: [05:02:32.801] 17  ConvHardSwish   batch_norm2d_16.b_0_deepcopy_82_65_bias   FLOAT     (256)          | 0x0032dd80 0x0032e180 0x00000400
D RKNN: [05:02:32.801] 18  ConvHardSwish   conv2d_17.w_0_deepcopy_85                 FLOAT16   (1,256,5,5)    | 0x00067f80 0x0006b180 0x00003200
D RKNN: [05:02:32.801] 18  ConvHardSwish   batch_norm2d_17.b_0_deepcopy_87_69_bias   FLOAT     (256)          | 0x0032e180 0x0032e580 0x00000400
D RKNN: [05:02:32.801] 19  ConvHardSwish   conv2d_18.w_0_deepcopy_90                 FLOAT16   (256,256,1,1)  | 0x0006b180 0x0008b180 0x00020000
D RKNN: [05:02:32.801] 19  ConvHardSwish   batch_norm2d_18.b_0_deepcopy_92_73_bias   FLOAT     (256)          | 0x0032e580 0x0032e980 0x00000400
D RKNN: [05:02:32.801] 20  ConvHardSwish   conv2d_19.w_0_deepcopy_95                 FLOAT16   (1,256,5,5)    | 0x0008b180 0x0008e380 0x00003200
D RKNN: [05:02:32.801] 20  ConvHardSwish   batch_norm2d_19.b_0_deepcopy_97_77_bias   FLOAT     (256)          | 0x0032e980 0x0032ed80 0x00000400
D RKNN: [05:02:32.801] 21  ConvHardSwish   conv2d_20.w_0_deepcopy_100                FLOAT16   (256,256,1,1)  | 0x0008e380 0x000ae380 0x00020000
D RKNN: [05:02:32.801] 21  ConvHardSwish   batch_norm2d_20.b_0_deepcopy_102_81_bias  FLOAT     (256)          | 0x0032ed80 0x0032f180 0x00000400
D RKNN: [05:02:32.801] 22  ConvHardSwish   conv2d_21.w_0_deepcopy_105                FLOAT16   (1,256,5,5)    | 0x000ae380 0x000b1580 0x00003200
D RKNN: [05:02:32.801] 22  ConvHardSwish   batch_norm2d_21.b_0_deepcopy_107_85_bias  FLOAT     (256)          | 0x0032f180 0x0032f580 0x00000400
D RKNN: [05:02:32.801] 23  ConvHardSwish   conv2d_22.w_0_deepcopy_110                FLOAT16   (256,256,1,1)  | 0x000b1580 0x000d1580 0x00020000
D RKNN: [05:02:32.801] 23  ConvHardSwish   batch_norm2d_22.b_0_deepcopy_112_89_bias  FLOAT     (256)          | 0x0032f580 0x0032f980 0x00000400
D RKNN: [05:02:32.801] 24  ConvHardSwish   conv2d_23.w_0_deepcopy_115                FLOAT16   (1,256,5,5)    | 0x000d1580 0x000d4780 0x00003200
D RKNN: [05:02:32.801] 24  ConvHardSwish   batch_norm2d_23.b_0_deepcopy_117_93_bias  FLOAT     (256)          | 0x0032f980 0x0032fd80 0x00000400
D RKNN: [05:02:32.801] 25  Conv            GlobalAveragePool.0_2conv0_i1             FLOAT16   (1,256,7,7)    | 0x00332480 0x00338680 0x00006200
D RKNN: [05:02:32.801] 25  Conv            GlobalAveragePool.0_2conv0_i2             FLOAT     (256)          | 0x00338680 0x00338a80 0x00000400
D RKNN: [05:02:32.801] 26  ConvRelu        conv2d_24.w_0_deepcopy_120                FLOAT16   (64,256,1,1)   | 0x000d4780 0x000dc780 0x00008000
D RKNN: [05:02:32.801] 26  ConvRelu        p2o.pd_op.conv2d.12.0_bias                FLOAT     (64)           | 0x0032fd80 0x0032fe80 0x00000100
D RKNN: [05:02:32.801] 27  ConvHardSigmoid conv2d_25.w_0_deepcopy_122                FLOAT16   (256,64,1,1)   | 0x000dc780 0x000e4780 0x00008000
D RKNN: [05:02:32.801] 27  ConvHardSigmoid p2o.pd_op.conv2d.13.0_bias                FLOAT     (256)          | 0x0032fe80 0x00330280 0x00000400
D RKNN: [05:02:32.801] 29  ConvHardSwish   conv2d_26.w_0_deepcopy_124                FLOAT16   (512,256,1,1)  | 0x000e4780 0x00124780 0x00040000
D RKNN: [05:02:32.801] 29  ConvHardSwish   batch_norm2d_24.b_0_deepcopy_126_108_bias FLOAT     (512)          | 0x00330280 0x00330a80 0x00000800
D RKNN: [05:02:32.801] 30  ConvHardSwish   conv2d_27.w_0_deepcopy_129                FLOAT16   (1,512,5,5)    | 0x00124780 0x0012ab80 0x00006400
D RKNN: [05:02:32.801] 30  ConvHardSwish   batch_norm2d_25.b_0_deepcopy_131_112_bias FLOAT     (512)          | 0x00330a80 0x00331280 0x00000800
D RKNN: [05:02:32.801] 31  Conv            GlobalAveragePool.1_2conv0_i1             FLOAT16   (1,512,7,7)    | 0x00338a80 0x00344e80 0x0000c400
D RKNN: [05:02:32.801] 31  Conv            GlobalAveragePool.1_2conv0_i2             FLOAT     (512)          | 0x00344e80 0x00345680 0x00000800
D RKNN: [05:02:32.801] 32  ConvRelu        conv2d_28.w_0_deepcopy_134                FLOAT16   (128,512,1,1)  | 0x0012ab80 0x0014ab80 0x00020000
D RKNN: [05:02:32.801] 32  ConvRelu        p2o.pd_op.conv2d.15.0_bias                FLOAT     (128)          | 0x00331280 0x00331480 0x00000200
D RKNN: [05:02:32.801] 33  ConvHardSigmoid conv2d_29.w_0_deepcopy_136                FLOAT16   (512,128,1,1)  | 0x0014ab80 0x0016ab80 0x00020000
D RKNN: [05:02:32.801] 33  ConvHardSigmoid p2o.pd_op.conv2d.16.0_bias                FLOAT     (512)          | 0x00331480 0x00331c80 0x00000800
D RKNN: [05:02:32.801] 35  ConvHardSwish   conv2d_30.w_0_deepcopy_138                FLOAT16   (512,512,1,1)  | 0x0016ab80 0x001eab80 0x00080000
D RKNN: [05:02:32.801] 35  ConvHardSwish   batch_norm2d_26.b_0_deepcopy_140_127_bias FLOAT     (512)        I rknn building done.
I Target is None, use simulator!
I GraphPreparing :   0%|                                                     | 0/72 [00:00<?, ?it/s]I GraphPreparing : 100%|█████████████████████████████████████████| 72/72 [00:00<00:00, 10714.18it/s]
I SessionPreparing :   0%|                                                   | 0/72 [00:00<?, ?it/s]I SessionPreparing : 100%|████████████████████████████████████████| 72/72 [00:00<00:00, 2279.43it/s]
{
  "model": "paddle_table_cls",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "Table/PP-LCNet_x1_0_table_cls.onnx",
  "onnx_md5": "83de43256e77c8cb5ac8eb57fecfbfe6",
  "rknn_file": "PP-LCNet_x1_0_table_cls_rk3588.rknn",
  "rknn_md5": "79583553c83de64b3d86a2a68d5ef90c",
  "rknn_bytes": 3956400,
  "input_names": [
    "x"
  ],
  "input_size": [
    [
      1,
      3,
      224,
      224
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      1,
      2
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "Table/PP-LCNet_x1_0_table_cls_rk3588.rknn",
  "hf_config_path": null,
  "config_md5": null
}
  | 0x00331c80 0x00332480 0x00000800
D RKNN: [05:02:32.801] 36  Conv            GlobalAveragePool.2_2conv0_i1             FLOAT16   (1,512,7,7)    | 0x00345680 0x00351a80 0x0000c400
D RKNN: [05:02:32.801] 36  Conv            GlobalAveragePool.2_2conv0_i2             FLOAT     (512)          | 0x00351a80 0x00352280 0x00000800
D RKNN: [05:02:32.801] 37  ConvHardSwish   conv2d_31.w_0_deepcopy_143                FLOAT16   (1280,512,1,1) | 0x001eab80 0x0032ab80 0x00140000
D RKNN: [05:02:32.801] 38  Conv            linear_0.w_0_deepcopy_144                 FLOAT16   (2,1280,1,1)   | 0x0032ab80 0x0032bf80 0x00001400
D RKNN: [05:02:32.801] 38  Conv            linear_0.b_0_deepcopy_145                 FLOAT     (2)            | 0x0032bf80 0x0032bfc0 0x00000040
D RKNN: [05:02:32.801] 40  Reshape         p2o.pd_op.matmul.0.0_rs_i1                INT64     (2)            | 0x00352280 0x00352290 0x00000010
D RKNN: [05:02:32.801] ---------------------------------------------------------------------------------------+---------------------------------
D RKNN: [05:02:32.801] ----------------------------------------
D RKNN: [05:02:32.801] Total Internal Memory Size: 4998KB
D RKNN: [05:02:32.801] Total Weight Memory Size: 3402.69KB
D RKNN: [05:02:32.801] ----------------------------------------
D RKNN: [05:02:32.801] <<<<<<<< end: rknn::RKNNMemStatisticsPass
```
