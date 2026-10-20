# RKNN conversion — slanet_plus (run 39372538918)

```json
{"status": "conversion failed before report"}
```

## conversion log (tail)
```
I rknn-toolkit2 version: 2.3.2
[1;33mW[0m [1;33mload_onnx: If you don't need to crop the model, don't set 'inputs'/'input_size_list'/'outputs'![0m
[1;33mW[0m [1;33mload_onnx: The config.mean_values is None, zeros will be set for input 0![0m
[1;33mW[0m [1;33mload_onnx: The config.std_values is None, ones will be set for input 0![0m
D base_optimize ...
[1;33mW[0m [1;33mbuild: onnx.checker.check_model fail: Unrecognized attribute: axes for operator ReduceMax

==> Context: Bad node spec for node. Name: Loop.0 OpType: Loop[0m
D base_optimize done.
D 
D fold_constant ...
[0;93m2026-10-20 05:02:21.239639918 [W:onnxruntime:Default, device_discovery.cc:133 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
[1;33mW[0m [1;33mbuild: onnx.checker.check_model fail: Unrecognized attribute: axes for operator ReduceMax

==> Context: Bad node spec for node. Name: Loop.0 OpType: Loop[0m
I Loading :   0%|                                                           | 0/484 [00:00<?, ?it/s]I Loading : 100%|█████████████████████████████████████████████| 484/484 [00:00<00:00, 442467.99it/s]
[1;31mE[0m [1;31mbuild: The Loop('Loop.0') will cause the graph to be a dynamic graph! Remove it manually and try again!
[0m
[1;33mW[0m [1;33mbuild: ===================== WARN(5) =====================[0m
[1;31mE[0m [1;31mrknn-toolkit2 version: 2.3.2[0m
[1;31mE[0m [1;31mbuild: Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 1990, in rknn.api.rknn_base.RKNNBase.build
  File "rknn/api/graph_optimizer.py", line 897, in rknn.api.graph_optimizer.GraphOptimizer.fold_constant
  File "rknn/api/graph_optimizer.py", line 372, in rknn.api.graph_optimizer._dynamic_check
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: The Loop('Loop.0') will cause the graph to be a dynamic graph! Remove it manually and try again!

[0m
I ===================== WARN(0) =====================
[1;31mE[0m [1;31mrknn-toolkit2 version: 2.3.2[0m
Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 1990, in rknn.api.rknn_base.RKNNBase.build
  File "rknn/api/graph_optimizer.py", line 897, in rknn.api.graph_optimizer.GraphOptimizer.fold_constant
  File "rknn/api/graph_optimizer.py", line 372, in rknn.api.graph_optimizer._dynamic_check
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: The Loop('Loop.0') will cause the graph to be a dynamic graph! Remove it manually and try again!


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 202, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 195, in main
    report = convert(args.model, spec, onnx_path, cache_dir, out_dir)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/MinerU-RK3588/MinerU-RK3588/tools/rk3588/convert.py", line 132, in convert
    if rknn.build(do_quantization=False) != 0:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/rknn/api/rknn.py", line 198, in build
    return self.rknn_base.build(do_quantization=do_quantization, dataset=dataset, expand_batch_size=rknn_batch_size, auto_hybrid=auto_hybrid)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "rknn/api/rknn_log.py", line 349, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: Traceback (most recent call last):
  File "rknn/api/rknn_log.py", line 344, in rknn.api.rknn_log.error_catch_decorator.error_catch_wrapper
  File "rknn/api/rknn_base.py", line 1990, in rknn.api.rknn_base.RKNNBase.build
  File "rknn/api/graph_optimizer.py", line 897, in rknn.api.graph_optimizer.GraphOptimizer.fold_constant
  File "rknn/api/graph_optimizer.py", line 372, in rknn.api.graph_optimizer._dynamic_check
  File "rknn/api/rknn_log.py", line 95, in rknn.api.rknn_log.RKNNLog.e
ValueError: The Loop('Loop.0') will cause the graph to be a dynamic graph! Remove it manually and try again!


```
