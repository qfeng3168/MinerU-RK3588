# RKNN conversion — ocr_det (run 39369951699)

```json
{"status": "conversion failed before report"}
```

## conversion log (tail)
```
D RKNN: [04:32:17.712] 107 Conv            GlobalAveragePool.4_2conv1_i2                  FLOAT     (16)          | 0x000d6d40 0x000d6dc0 0x00000080
D RKNN: [04:32:17.712] 108 ConvRelu        conv2d_98.w_0                                  FLOAT16   (4,16,1,1)    | 0x000c62c0 0x000c6340 0x00000080
D RKNN: [04:32:17.712] 108 ConvRelu        _v_869                                         FLOAT     (4)           | 0x000d4100 0x000d4140 0x00000040
D RKNN: [04:32:17.712] 109 ConvHardSigmoid conv2d_99.w_0                                  FLOAT16   (16,4,1,1)    | 0x000c6340 0x000c6440 0x00000100
D RKNN: [04:32:17.712] 109 ConvHardSigmoid _v_872                                         FLOAT     (16)          | 0x000d4140 0x000d4180 0x00000040
D RKNN: [04:32:17.712] 112 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [04:32:17.712] 112 Resize          helper.constant.39                             FLOAT     (4)           | 0x000c4dc0 0x000c4e40 0x00000080
D RKNN: [04:32:17.712] 114 Conv            conv2d_164.w_0                                 FLOAT16   (1,64,5,5)    | 0x000c6440 0x000c70c0 0x00000c80
D RKNN: [04:32:17.712] 114 Conv            _v_875                                         FLOAT     (64)          | 0x000d4180 0x000d4280 0x00000100
D RKNN: [04:32:17.712] 115 Conv            conv2d_88.w_0                                  FLOAT16   (16,64,1,1)   | 0x000c70c0 0x000c78c0 0x00000800
D RKNN: [04:32:17.712] 116 Conv            GlobalAveragePool.5_2conv0_i1                  FLOAT16   (1,16,7,7)    | 0x000d9a40 0x000da060 0x00000620
D RKNN: [04:32:17.712] 116 Conv            GlobalAveragePool.5_2conv0_i2                  FLOAT     (16)          | 0x000da080 0x000da100 0x00000080
D RKNN: [04:32:17.712] 117 Conv            GlobalAveragePool.5_2conv1_i1                  FLOAT16   (1,16,6,6)    | 0x000da100 0x000da580 0x00000480
D RKNN: [04:32:17.712] 117 Conv            GlobalAveragePool.5_2conv1_i2                  FLOAT     (16)          | 0x000da580 0x000da600 0x00000080
D RKNN: [04:32:17.712] 118 ConvRelu        conv2d_89.w_0                                  FLOAT16   (4,16,1,1)    | 0x000c78c0 0x000c7940 0x00000080
D RKNN: [04:32:17.712] 118 ConvRelu        _v_878                                         FLOAT     (4)           | 0x000d4280 0x000d42c0 0x00000040
D RKNN: [04:32:17.712] 119 ConvHardSigmoid conv2d_90.w_0                                  FLOAT16   (16,4,1,1)    | 0x000c7940 0x000c7a40 0x00000100
D RKNN: [04:32:17.712] 119 ConvHardSigmoid _v_881                                         FLOAT     (16)          | 0x000d42c0 0x000d4300 0x00000040
D RKNN: [04:32:17.712] 122 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [04:32:17.712] 122 Resize          helper.constant.39                             FLOAT     (4)           | 0x000c4dc0 0x000c4e40 0x00000080
D RKNN: [04:32:17.712] 124 Conv            conv2d_163.w_0                                 FLOAT16   (1,64,5,5)    | 0x000c7a40 0x000c86c0 0x00000c80
D RKNN: [04:32:17.712] 124 Conv            _v_884                                         FLOAT     (64)          | 0x000d4300 0x000d4400 0x00000100
D RKNN: [04:32:17.712] 125 Conv            conv2d_79.w_0                                  FLOAT16   (16,64,1,1)   | 0x000c86c0 0x000c8ec0 0x00000800
D RKNN: [04:32:17.712] 126 Conv            GlobalAveragePool.6_2conv0_i1                  FLOAT16   (1,16,7,7)    | 0x000ddc00 0x000de220 0x00000620
D RKNN: [04:32:17.712] 126 Conv            GlobalAveragePool.6_2conv0_i2                  FLOAT     (16)          | 0x000de240 0x000de2c0 0x00000080
D RKNN: [04:32:17.712] 127 Conv            GlobalAveragePool.6_2conv1_i1                  FLOAT16   (1,16,7,7)    | 0x000de2c0 0x000de8e0 0x00000620
D RKNN: [04:32:17.712] 127 Conv            GlobalAveragePool.6_2conv1_i2                  FLOAT     (16)          | 0x000de900 0x000de980 0x00000080
D RKNN: [04:32:17.712] 128 Conv            GlobalAveragePool.6_2conv2_i1                  FLOAT16   (1,16,2,2)    | 0x000de980 0x000dea00 0x00000080
D RKNN: [04:32:17.712] 128 Conv            GlobalAveragePool.6_2conv2_i2                  FLOAT     (16)          | 0x000dea00 0x000dea80 0x00000080
D RKNN: [04:32:17.712] 129 ConvRelu        conv2d_80.w_0                                  FLOAT16   (4,16,1,1)    | 0x000c8ec0 0x000c8f40 0x00000080
D RKNN: [04:32:17.712] 129 ConvRelu        _v_887                                         FLOAT     (4)           | 0x000d4400 0x000d4440 0x00000040
D RKNN: [04:32:17.712] 130 ConvHardSigmoid conv2d_81.w_0                                  FLOAT16   (16,4,1,1)    | 0x000c8f40 0x000c9040 0x00000100
D RKNN: [04:32:17.712] 130 ConvHardSigmoid _v_890                                         FLOAT     (16)          | 0x000d4440 0x000d4480 0x00000040
D RKNN: [04:32:17.712] 133 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [04:32:17.712] 133 Resize          helper.constant.39                             FLOAT     (4)           | 0x000c4dc0 0x000c4e40 0x00000080
D RKNN: [04:32:17.712] 135 Conv            conv2d_162.w_0                                 FLOAT16   (1,64,5,5)    | 0x000c9040 0x000c9cc0 0x00000c80
D RKNN: [04:32:17.712] 135 Conv            _v_893                                         FLOAT     (64)          | 0x000d4480 0x000d4580 0x00000100
D RKNN: [04:32:17.712] 136 Conv            conv2d_70.w_0                                  FLOAT16   (16,64,1,1)   | 0x000c9cc0 0x000ca4c0 0x00000800
D RKNN: [04:32:17.712] 137 Conv            GlobalAveragePool.7_2conv0_i1                  FLOAT16   (1,16,7,7)    | 0x000e2680 0x000e2ca0 0x00000620
D RKNN: [04:32:17.712] 137 Conv            GlobalAveragePool.7_2conv0_i2                  FLOAT     (16)          | 0x000e2cc0 0x000e2d40 0x00000080
D RKNN: [04:32:17.712] 138 Conv            GlobalAveragePool.7_2conv1_i1                  FLOAT16   (1,16,7,7)    | 0x000e2d40 0x000e3360 0x00000620
D RKNN: [04:32:17.712] 138 Conv            GlobalAveragePool.7_2conv1_i2                  FLOAT     (16)          | 0x000e3380 0x000e3400 0x00000080
D RKNN: [04:32:17.712] 139 Conv            GlobalAveragePool.7_2conv2_i1                  FLOAT16   (1,16,4,4)    | 0x000e3400 0x000e3600 0x00000200
D RKNN: [04:32:17.712] 139 Conv            GlobalAveragePool.7_2conv2_i2                  FLOAT     (16)          | 0x000e3600 0x000e3680 0x00000080
D RKNN: [04:32:17.712] 140 ConvRelu        conv2d_71.w_0                                  FLOAT16   (4,16,1,1)    | 0x000ca4c0 0x000ca540 0x00000080
D RKNN: [04:32:17.712] 140 ConvRelu        _v_896                                         FLOAT     (4)           | 0x000d4580 0x000d45c0 0x00000040
D RKNN: [04:32:17.712] 141 ConvHardSigmoid conv2d_72.w_0                                  FLOAT16   (16,4,1,1)    | 0x000ca540 0x000ca640 0x00000100
D RKNN: [04:32:17.712] 141 ConvHardSigmoid _v_899                                         FLOAT     (16)          | 0x000d45c0 0x000d4600 0x00000040
D RKNN: [04:32:17.712] 144 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [04:32:17.712] 144 Resize          helper.constant.45                             FLOAT     (4)           | 0x000ca640 0x000ca6c0 0x00000080
D RKNN: [04:32:17.712] 145 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [04:32:17.712] 145 Resize          helper.constant.47                             FLOAT     (4)           | 0x000ca6c0 0x000ca740 0x00000080
D RKNN: [04:32:17.712] 146 Resize          helper.constant.40                             FLOAT     (0)           | 0x000c4dc0 0x000c4dc0 0x00000000
D RKNN: [04:32:17.712] 146 Resize          helper.constant.39                             FLOAT     (4)           | 0x000c4dc0 0x000c4e40 0x00000080
D RKNN: [04:32:17.712] 148 ConvRelu        conv2d_166.w_0                                 FLOAT16   (16,64,3,3)   | 0x000ca740 0x000cef40 0x00004800
D RKNN: [04:32:17.71I rknn building done.
I Target is None, use simulator!
[1;33mW[0m [1;33minference: The 'data_format' is not set, and its default value is 'nhwc'![0m
I GraphPreparing :   0%|                                                    | 0/209 [00:00<?, ?it/s]I GraphPreparing : 100%|███████████████████████████████████████| 209/209 [00:00<00:00, 22861.12it/s]
I SessionPreparing :   0%|                                                  | 0/209 [00:00<?, ?it/s]I SessionPreparing : 100%|██████████████████████████████████████| 209/209 [00:00<00:00, 3812.84it/s]
[1;31mE[0m [1;31minference: The input(ndarray) shape (1, 3, 640, 640) is wrong, expect 'nhwc' like (1, 640, 640, 3)![0m
[1;33mW[0m [1;33minference: ===================== WARN(4) =====================[0m
[1;31mE[0m [1;31mrknn-toolkit2 version: 2.3.2[0m
[1;31mE[0m [1;31minference: Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 2707, in rknn.api.rknn_base.RKNNBase.inference
  File "rknn/api/simulator.py", line 592, in rknn.api.simulator.Simulator.inference
  File "rknn/api/simulator.py", line 554, in rknn.api.simulator.Simulator._get_inputs
  File "rknn/api/rknn_utils.py", line 328, in rknn.api.rknn_utils.get_input_img
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: The input(ndarray) shape (1, 3, 640, 640) is wrong, expect 'nhwc' like (1, 640, 640, 3)!
[0m
I ===================== WARN(0) =====================
[1;31mE[0m [1;31mrknn-toolkit2 version: 2.3.2[0m
2] 148 ConvRelu        _v_902                                         FLOAT     (16)          | 0x000d4600 0x000d4640 0x00000040
D RKNN: [04:32:17.712] 149 ConvTranspose   auto.cast.95                                   FLOAT16   (16,16,2,2)   | 0x000cef40 0x000cf740 0x00000800
D RKNN: [04:32:17.712] 150 AddRelu         p2o.pd_op.reshape.75.0                         FLOAT     (1,16,1,1)    | 0x000cf740 0x000cf780 0x00000040
D RKNN: [04:32:17.712] 151 ConvTranspose   auto.cast.98                                   FLOAT16   (16,1,2,2)    | 0x000cf780 0x000cf800 0x00000080
D RKNN: [04:32:17.712] 152 Add             p2o.pd_op.reshape.76.0                         FLOAT     (1,1,1,1)     | 0x000cf800 0x000cf840 0x00000040
D RKNN: [04:32:17.712] -------------------------------------------------------------------------------------------+---------------------------------
D RKNN: [04:32:17.712] ----------------------------------------
D RKNN: [04:32:17.712] Total Internal Memory Size: 20000KB
D RKNN: [04:32:17.712] Total Weight Memory Size: 971.125KB
D RKNN: [04:32:17.712] ----------------------------------------
D RKNN: [04:32:17.712] <<<<<<<< end: rknn::RKNNMemStatisticsPass
Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 2707, in rknn.api.rknn_base.RKNNBase.inference
  File "rknn/api/simulator.py", line 592, in rknn.api.simulator.Simulator.inference
  File "rknn/api/simulator.py", line 554, in rknn.api.simulator.Simulator._get_inputs
  File "rknn/api/rknn_utils.py", line 328, in rknn.api.rknn_utils.get_input_img
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: The input(ndarray) shape (1, 3, 640, 640) is wrong, expect 'nhwc' like (1, 640, 640, 3)!

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 160, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 153, in main
    report = convert(args.model, spec, onnx_path, out_dir)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 119, in convert
    outputs = rknn.inference(inputs=dummy)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/rknn/api/rknn.py", line 314, in inference
    return self.rknn_base.inference(inputs=inputs, data_format=data_format,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "rknn/api/rknn_log.py", line 349, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 2707, in rknn.api.rknn_base.RKNNBase.inference
  File "rknn/api/simulator.py", line 592, in rknn.api.simulator.Simulator.inference
  File "rknn/api/simulator.py", line 554, in rknn.api.simulator.Simulator._get_inputs
  File "rknn/api/rknn_utils.py", line 328, in rknn.api.rknn_utils.get_input_img
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: The input(ndarray) shape (1, 3, 640, 640) is wrong, expect 'nhwc' like (1, 640, 640, 3)!

```
