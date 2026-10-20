# RKNN conversion — unet_structure (run 39371282526)

```json
{
  "model": "unet_structure",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "Table/unet.onnx",
  "onnx_md5": "252e4ee3c05690a7ec1d92423eb071cc",
  "rknn_file": "unet_rk3588.rknn",
  "rknn_md5": "8f711e5c1c1543fc6721568aec4af431",
  "rknn_bytes": 10498422,
  "input_names": [
    "input"
  ],
  "input_size": [
    [
      1,
      3,
      768,
      768
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      1,
      1,
      768,
      768
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "Table/unet_rk3588.rknn",
  "hf_config_path": null,
  "config_md5": null
}```

## conversion log (tail)
```
D RKNN: [04:47:08.868] 53  ConvRelu               719                                       FLOAT16   (128,128,1,3) | 0x00314d00 0x0032cd00 0x00018000
D RKNN: [04:47:08.868] 53  ConvRelu               720                                       FLOAT     (128)         | 0x0032cd00 0x0032cf00 0x00000200
D RKNN: [04:47:08.868] 54  ConvRelu               backbone.encoder.12.convs_layers.5.weight FLOAT16   (128,128,3,1) | 0x0012bb80 0x00143b80 0x00018000
D RKNN: [04:47:08.868] 54  ConvRelu               backbone.encoder.12.convs_layers.5.bias   FLOAT     (128)         | 0x00143b80 0x00143d80 0x00000200
D RKNN: [04:47:08.868] 55  ConvAddRelu            722                                       FLOAT16   (128,128,1,3) | 0x0032cf00 0x00344f00 0x00018000
D RKNN: [04:47:08.868] 55  ConvAddRelu            723                                       FLOAT     (128)         | 0x00344f00 0x00345100 0x00000200
D RKNN: [04:47:08.868] 56  ConvRelu               backbone.encoder.13.convs_layers.0.weight FLOAT16   (128,128,3,1) | 0x00143d80 0x0015bd80 0x00018000
D RKNN: [04:47:08.868] 56  ConvRelu               backbone.encoder.13.convs_layers.0.bias   FLOAT     (128)         | 0x0015bd80 0x0015bf80 0x00000200
D RKNN: [04:47:08.868] 57  ConvRelu               725                                       FLOAT16   (128,128,1,3) | 0x00345100 0x0035d100 0x00018000
D RKNN: [04:47:08.868] 57  ConvRelu               726                                       FLOAT     (128)         | 0x0035d100 0x0035d300 0x00000200
D RKNN: [04:47:08.868] 58  ConvRelu               backbone.encoder.13.convs_layers.5.weight FLOAT16   (128,128,3,1) | 0x0015bf80 0x00173f80 0x00018000
D RKNN: [04:47:08.868] 58  ConvRelu               backbone.encoder.13.convs_layers.5.bias   FLOAT     (128)         | 0x00173f80 0x00174180 0x00000200
D RKNN: [04:47:08.868] 59  ConvAddRelu            728                                       FLOAT16   (128,128,1,3) | 0x0035d300 0x00375300 0x00018000
D RKNN: [04:47:08.868] 59  ConvAddRelu            729                                       FLOAT     (128)         | 0x00375300 0x00375500 0x00000200
D RKNN: [04:47:08.868] 60  ConvRelu               backbone.encoder.14.convs_layers.0.weight FLOAT16   (128,128,3,1) | 0x00174180 0x0018c180 0x00018000
D RKNN: [04:47:08.868] 60  ConvRelu               backbone.encoder.14.convs_layers.0.bias   FLOAT     (128)         | 0x0018c180 0x0018c380 0x00000200
D RKNN: [04:47:08.868] 61  ConvRelu               731                                       FLOAT16   (128,128,1,3) | 0x00375500 0x0038d500 0x00018000
D RKNN: [04:47:08.868] 61  ConvRelu               732                                       FLOAT     (128)         | 0x0038d500 0x0038d700 0x00000200
D RKNN: [04:47:08.868] 62  ConvRelu               backbone.encoder.14.convs_layers.5.weight FLOAT16   (128,128,3,1) | 0x0018c380 0x001a4380 0x00018000
D RKNN: [04:47:08.868] 62  ConvRelu               backbone.encoder.14.convs_layers.5.bias   FLOAT     (128)         | 0x001a4380 0x001a4580 0x00000200
D RKNN: [04:47:08.868] 63  ConvAddRelu            734                                       FLOAT16   (128,128,1,3) | 0x0038d700 0x003a5700 0x00018000
D RKNN: [04:47:08.868] 63  ConvAddRelu            735                                       FLOAT     (128)         | 0x003a5700 0x003a5900 0x00000200
D RKNN: [04:47:08.868] 64  ConvRelu               backbone.encoder.15.convs_layers.0.weight FLOAT16   (128,128,3,1) | 0x001a4580 0x001bc580 0x00018000
D RKNN: [04:47:08.868] 64  ConvRelu               backbone.encoder.15.convs_layers.0.bias   FLOAT     (128)         | 0x001bc580 0x001bc780 0x00000200
D RKNN: [04:47:08.868] 65  ConvRelu               737                                       FLOAT16   (128,128,1,3) | 0x003a5900 0x003bd900 0x00018000
D RKNN: [04:47:08.868] 65  ConvRelu               738                                       FLOAT     (128)         | 0x003bd900 0x003bdb00 0x00000200
D RKNN: [04:47:08.868] 66  Pad                    558_pad_i1                                INT64     (8)           | 0x003f9740 0x003f9780 0x00000040
D RKNN: [04:47:08.868] 67  ConvRelu               backbone.encoder.15.convs_layers.5.weight FLOAT16   (128,128,3,1) | 0x001bc780 0x001d4780 0x00018000
D RKNN: [04:47:08.868] 67  ConvRelu               backbone.encoder.15.convs_layers.5.bias   FLOAT     (128)         | 0x001d4780 0x001d4980 0x00000200
D RKNN: [04:47:08.868] 68  Pad                    560_pad_i1                                INT64     (8)           | 0x003f9780 0x003f97c0 0x00000040
D RKNN: [04:47:08.868] 69  ConvAddRelu            740                                       FLOAT16   (128,128,1,3) | 0x003bdb00 0x003d5b00 0x00018000
D RKNN: [04:47:08.868] 69  ConvAddRelu            741                                       FLOAT     (128)         | 0x003d5b00 0x003d5d00 0x00000200
D RKNN: [04:47:08.868] 70  ConvTransposeRelu      backbone.decoder.0.conv.weight            FLOAT16   (128,64,3,3)  | 0x001d4980 0x001f8980 0x00024000
D RKNN: [04:47:08.868] 70  ConvTransposeRelu      backbone.decoder.0.conv.bias              FLOAT     (64)          | 0x001f8980 0x001f8a80 0x00000100
D RKNN: [04:47:08.868] 71  ConvRelu               backbone.decoder.1.convs_layers.0.weight  FLOAT16   (64,64,3,1)   | 0x001f8a80 0x001fea80 0x00006000
D RKNN: [04:47:08.868] 71  ConvRelu               backbone.decoder.1.convs_layers.0.bias    FLOAT     (64)          | 0x001fea80 0x001feb80 0x00000100
D RKNN: [04:47:08.868] 72  ConvRelu               743                                       FLOAT16   (64,64,1,3)   | 0x003d5d00 0x003dbd00 0x00006000
D RKNN: [04:47:08.868] 72  ConvRelu               744                                       FLOAT     (64)          | 0x003dbd00 0x003dbe00 0x00000100
D RKNN: [04:47:08.868] 73  ConvRelu               backbone.decoder.1.convs_layers.5.weight  FLOAT16   (64,64,3,1)   | 0x001feb80 0x00204b80 0x00006000
D RKNN: [04:47:08.868] 73  ConvRelu               backbone.decoder.1.convs_layers.5.bias    FLOAT     (64)          | 0x00204b80 0x00204c80 0x00000100
D RKNN: [04:47:08.868] 74  ConvAddRelu            746                                       FLOAT16   (64,64,1,3)   | 0x003dbe00 0x003e1e00 0x00006000
D RKNN: [04:47:08.868] 74  ConvAddRelu            747                                       FLOAT     (64)          | 0x003e1e00 0x003e1f00 0x00000100
D RKNN: [04:47:08.868] 75  ConvRelu               backbone.decoder.2.convs_layers.0.weight  FLOAT16   (64,64,3,1)   | 0x00204c80 0x0020ac80 0x00006000
D RKNN: [04:47:08.868] 75  ConvRelu               backbone.decoder.2.convs_layers.0.bias    FLOAT     (64)          | 0x0020ac80 0x0020ad80 0x00000100
D RKNN: [04:47:08.868] 76  ConvRelu               749                                       FLOAT16   (64,64,1,3)   | 0x003e1f00 0x003e7f00 0x00006000
D RKNN: [04:47:08.868] 76  ConvRelu               750                                       FLOAT     (64)          | 0x003e7f00 0x003e8000 0x00000100
D RKNN: [04:47:08.868] 77  ConvRelu               backbone.decoder.2.convs_layers.5.weight  FLOAT16   (64,64,3,1)   | 0x0020ad80 0x00210d80 0x00006000
D RKNN: [04:47:08.868] 77  ConvRelu               backbone.decoder.2.convs_layers.5.bias    FLOAT     (64)          | 0x00210d80 0x00210e80 0x00000100
D RKNN: [04:47:08.868] 78  ConvAddRelu            752                                       FLOAT16   (64,64,1,3)   | 0x003e8000 0x003ee000 0x00006000
D RKNN: [04:47:08.868] 78  ConvAddRelu            753                                       FLOAT     (64)          | 0x003ee000 0x003ee100 0x00000100
D RKNN: [04:47:08.868] 79  ConvTransposeRelu      backbone.decoder.3.conv.weight            FLOAT16   (64,16,3,3)   | 0x00210e80 0x00215680 0x00004800
D RKNN: [04:47:08.868] 79  ConvTransposeRelu      backbone.decoder.3.conv.bias              FLOAT     (16)          | 0x00215680 0x002156c0 0x00000040
D RKNN: [04:47:08.868] 80  ConvRelu               backbone.decoder.4.convs_layers.0.weight  FLOAT16   (16,16,3,1)   | 0x002156c0 0x00215cc0 0x00000600
D RKNN: [04:47:08.868] 80  ConvRelu               backbone.decoder.4.convs_layers.0.bias    FLOAT     (16)          | 0x00215cc0 0x00215d00 0x00000040
D RKNN: [04:47:08.868] 81  ConvRelu               755                                       FLOAT16   (16,16,1,3)   | 0x003ee100 0x003ee700 0x00000600
D RKNN: [04:47:08.868] 81  ConvRelu               756                                       FLOAT     (16)          | 0x003ee700 0x003ee740 0x00000040
D RKNN: [04:47:08.868] 82  ConvRelu               backbone.decoder.4.convs_layers.5.weight  FLOAT16   (16,16,3,1)   | 0x00215d00 0x00216300 0x00000600
D RKNN: [04:47:08.868] 82  ConvRelu               backbone.decoder.4.convs_layers.5.bias    FLOAT     (16)          | 0x00216300 0x00216340 0x00000040
D RKNN: [04:47:08.868] 83  ConvAddRelu            758                                       FLOAT16   (16,16,1,3)   | 0x003ee740 0x003eed40 0x00000600
D RKNN: [04:47:08.868] 83  ConvAddRelu            759                                       FLOAT     (16)          | 0x003eed40 0x003eed80 0x00000040
D RKNN: [04:47:08.868] 84  ConvRelu               backbone.decoder.5.convs_layers.0.weight  FLOAT16   (16,16,3,1)   | 0x00216340 0x00216940 0x00000600
D RKNN: [04:47:08.868] 84  ConvRelu               backbone.decoder.5.convs_layers.0.bias    FLOAT     (16)          | 0x00216940 0x00216980 0x00000040
D RKNN: [04:47:08.868] 85  ConvRelu               761                                       FLOAT16   (16,16,1,3)   | 0x003eed80 0x003ef380 0x00000600
D RKNN: [04:47:08.868] 85  ConvRelu               762                                       FLOAT     (16)          | 0x003ef380 0x003ef3c0 0x00000040
D RKNN: [04:47:08.868] 86  ConvRelu               backbone.decoder.5.convs_layers.5.weight  FLOAT16   (16,16,3,1)   | 0x00216980 0x00216f80 0x00000600
D RKNN: [04:47:08.868] 86  ConvRelu               backbone.decoder.5.convs_layers.5.bias    FLOAT     (16)          | 0x00216f80 0x00216fc0 0x00000040
D RKNN: [04:47:08.868] 87  ConvAddRelu            764                                       FLOAT16   I rknn building done.
I Target is None, use simulator!
I GraphPreparing :   0%|                                                    | 0/185 [00:00<?, ?it/s]I GraphPreparing : 100%|███████████████████████████████████████| 185/185 [00:00<00:00, 10935.75it/s]
I SessionPreparing :   0%|                                                  | 0/185 [00:00<?, ?it/s]I SessionPreparing : 100%|██████████████████████████████████████| 185/185 [00:00<00:00, 3143.12it/s]
{
  "model": "unet_structure",
  "onnx_repo": "opendatalab/MinerU-4_models_onnx",
  "onnx_path": "Table/unet.onnx",
  "onnx_md5": "252e4ee3c05690a7ec1d92423eb071cc",
  "rknn_file": "unet_rk3588.rknn",
  "rknn_md5": "8f711e5c1c1543fc6721568aec4af431",
  "rknn_bytes": 10498422,
  "input_names": [
    "input"
  ],
  "input_size": [
    [
      1,
      3,
      768,
      768
    ]
  ],
  "quantization": "none (fp)",
  "selfcheck_output_shapes": [
    [
      1,
      1,
      768,
      768
    ]
  ],
  "hf_repo": "q81801/MinerU-RK3588-models",
  "hf_rknn_path": "Table/unet_rk3588.rknn",
  "hf_config_path": null,
  "config_md5": null
}
(16,16,1,3)   | 0x003ef3c0 0x003ef9c0 0x00000600
D RKNN: [04:47:08.868] 87  ConvAddRelu            765                                       FLOAT     (16)          | 0x003ef9c0 0x003efa00 0x00000040
D RKNN: [04:47:08.868] 88  ConvRelu               767                                       FLOAT16   (128,16,3,3)  | 0x003efa00 0x003f8a00 0x00009000
D RKNN: [04:47:08.868] 88  ConvRelu               768                                       FLOAT     (128)         | 0x003f8a00 0x003f8c00 0x00000200
D RKNN: [04:47:08.868] 89  Conv                   decode_head.conv_seg.weight               FLOAT16   (3,128,1,1)   | 0x00216fc0 0x002172c0 0x00000300
D RKNN: [04:47:08.868] 89  Conv                   decode_head.conv_seg.bias                 FLOAT     (3)           | 0x002172c0 0x00217300 0x00000040
D RKNN: [04:47:08.868] 90  Resize                 628                                       FLOAT     (0)           | 0x003f8c40 0x003f8c40 0x00000000
D RKNN: [04:47:08.868] 90  Resize                 empty_placeholder_0                       FLOAT     (1)           | 0x003f97c0 0x003f9840 0x00000080
D RKNN: [04:47:08.868] 90  Resize                 635                                       INT64     (4)           | 0x003f8c40 0x003f8c60 0x00000020
D RKNN: [04:47:08.868] 91  ReduceMax              ReduceMax_272_axes                        INT64     (1)           | 0x003f8c00 0x003f8c08 0x00000008
D RKNN: [04:47:08.868] 92  Conv                   657_conv_i1                               FLOAT16   (3,1,1,1)     | 0x003f9680 0x003f96b0 0x00000030
D RKNN: [04:47:08.868] ---------------------------------------------------------------------------------------------+---------------------------------
D RKNN: [04:47:08.869] ----------------------------------------
D RKNN: [04:47:08.869] Total Internal Memory Size: 117528KB
D RKNN: [04:47:08.869] Total Weight Memory Size: 4072.12KB
D RKNN: [04:47:08.869] ----------------------------------------
D RKNN: [04:47:08.869] <<<<<<<< end: rknn::RKNNMemStatisticsPass
```
