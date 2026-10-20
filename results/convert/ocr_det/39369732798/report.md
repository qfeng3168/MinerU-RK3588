# RKNN conversion — ocr_det (run 39369732798)

```json
{"status": "conversion failed before report"}
```

## conversion log (tail)
```
I rknn-toolkit2 version: 2.3.2
[1;33mW[0m [1;33mload_onnx: If you don't need to crop the model, don't set 'inputs'/'input_size_list'/'outputs'![0m
[1;31mE[0m [1;31mload_onnx: Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 1579, in rknn.api.rknn_base.RKNNBase.load_onnx
  File "rknn/api/rknn_base.py", line 613, in rknn.api.rknn_base.RKNNBase._create_ir_and_inputs_meta
  File "rknn/api/ir_graph.py", line 84, in rknn.api.ir_graph.IRGraph.__init__
  File "rknn/api/ir_graph.py", line 475, in rknn.api.ir_graph.IRGraph.rebuild
  File "rknn/api/base_utils.py", line 31, in rknn.api.base_utils.to_tensor_type
AttributeError: module 'onnx' has no attribute 'mapping'
[0m
[1;33mW[0m [1;33mload_onnx: ===================== WARN(1) =====================[0m
[1;31mE[0m [1;31mrknn-toolkit2 version: 2.3.2[0m
Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 1579, in rknn.api.rknn_base.RKNNBase.load_onnx
  File "rknn/api/rknn_base.py", line 613, in rknn.api.rknn_base.RKNNBase._create_ir_and_inputs_meta
  File "rknn/api/ir_graph.py", line 84, in rknn.api.ir_graph.IRGraph.__init__
  File "rknn/api/ir_graph.py", line 475, in rknn.api.ir_graph.IRGraph.rebuild
  File "rknn/api/base_utils.py", line 31, in rknn.api.base_utils.to_tensor_type
AttributeError: module 'onnx' has no attribute 'mapping'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 160, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 153, in main
    report = convert(args.model, spec, onnx_path, out_dir)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 108, in convert
    if rknn.load_onnx(model=str(onnx_path), inputs=input_names, input_size_list=spec.input_size) != 0:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/rknn/api/rknn.py", line 168, in load_onnx
    return self.rknn_base.load_onnx(model, inputs, input_size_list, input_initial_val, outputs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "rknn/api/rknn_log.py", line 349, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 1579, in rknn.api.rknn_base.RKNNBase.load_onnx
  File "rknn/api/rknn_base.py", line 613, in rknn.api.rknn_base.RKNNBase._create_ir_and_inputs_meta
  File "rknn/api/ir_graph.py", line 84, in rknn.api.ir_graph.IRGraph.__init__
  File "rknn/api/ir_graph.py", line 475, in rknn.api.ir_graph.IRGraph.rebuild
  File "rknn/api/base_utils.py", line 31, in rknn.api.base_utils.to_tensor_type
AttributeError: module 'onnx' has no attribute 'mapping'

```
