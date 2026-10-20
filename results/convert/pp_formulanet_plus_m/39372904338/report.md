# RKNN conversion — pp_formulanet_plus_m (run 39372904338)

```json
{"status": "conversion failed before report"}
```

## conversion log (tail)
```
I rknn-toolkit2 version: 2.3.2
[1;33mW[0m [1;33mload_onnx: If you don't need to crop the model, don't set 'inputs'/'input_size_list'/'outputs'![0m
I Loading :   0%|                                                           | 0/522 [00:00<?, ?it/s]I Loading :  69%|████████████████████████████████▏              | 358/522 [00:00<00:00, 3267.14it/s]I Loading : 100%|███████████████████████████████████████████████| 522/522 [00:00<00:00, 1490.49it/s]
[1;31mE[0m [1;31mload_onnx: Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 1579, in rknn.api.rknn_base.RKNNBase.load_onnx
  File "rknn/api/rknn_base.py", line 618, in rknn.api.rknn_base.RKNNBase._create_ir_and_inputs_meta
  File "rknn/api/ir_graph.py", line 2131, in rknn.api.ir_graph.IRGraph.convert_to_fp32
AttributeError: 'numpy.ndarray' object has no attribute 'data_type'
[0m
[1;33mW[0m [1;33mload_onnx: ===================== WARN(1) =====================[0m
[1;31mE[0m [1;31mrknn-toolkit2 version: 2.3.2[0m
Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 1579, in rknn.api.rknn_base.RKNNBase.load_onnx
  File "rknn/api/rknn_base.py", line 618, in rknn.api.rknn_base.RKNNBase._create_ir_and_inputs_meta
  File "rknn/api/ir_graph.py", line 2131, in rknn.api.ir_graph.IRGraph.convert_to_fp32
AttributeError: 'numpy.ndarray' object has no attribute 'data_type'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 202, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 195, in main
    report = convert(args.model, spec, onnx_path, cache_dir, out_dir)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 130, in convert
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
  File "rknn/api/rknn_base.py", line 618, in rknn.api.rknn_base.RKNNBase._create_ir_and_inputs_meta
  File "rknn/api/ir_graph.py", line 2131, in rknn.api.ir_graph.IRGraph.convert_to_fp32
AttributeError: 'numpy.ndarray' object has no attribute 'data_type'

```
