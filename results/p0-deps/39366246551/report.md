# RK3588 Phase 0 — aarch64 deps check (run 39366246551)

- runner: ubuntu-24.04-arm, python 3.11 (board mirror: Debian 12 / py3.11)
- binary-only resolution: failure
- full install step: success
- smoke test: success

## binary-only check (deps lacking aarch64 wheels show up here)
```
ERROR: Could not find a version that satisfies the requirement jieba>=0.42.1 (from mineru) (from versions: none)
ERROR: No matching distribution found for jieba>=0.42.1
```

## installed key packages
```
docvortex==0.5.16
gradio==6.30.0
gradio_client==2.7.2
hf-gradio==0.4.1
mineru==4.0.12
mineru-llama-cpp==0.1.3
mineru_vl_utils==2.0.7
numpy==2.4.6
onnxruntime==1.31.0
pillow==12.3.0
pyclipper==1.4.0
pypdfium2==5.14.0
shapely==2.2.0
tokenizers==0.23.3
```

## smoke output
```
[0;93m2026-10-20 03:49:49.665086353 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
onnxruntime 1.31.0 ['AzureExecutionProvider', 'CPUExecutionProvider']
mineru import OK
[1m                                                                                [0m
[1m [0m[1;33mUsage: [0m[1mmineru [OPTIONS] COMMAND [ARGS]...[0m[1m                                     [0m[1m [0m
[1m                                                                                [0m
 MinerU — your personal document center, built for agents                       
                                                                                
[2m╭─[0m[2m Options [0m[2m───────────────────────────────────────────────────────────────────[0m[2m─╮[0m
[2m│[0m [1;36m-[0m[1;36m-version[0m          Show the version and exit.                                [2m│[0m
[2m│[0m [1;36m-[0m[1;36m-help[0m             Show this message and exit.                               [2m│[0m
[2m╰──────────────────────────────────────────────────────────────────────────────╯[0m
[2m╭─[0m[2m Commands [0m[2m──────────────────────────────────────────────────────────────────[0m[2m─╮[0m
[2m│[0m [1;36mparse     [0m[1;36m [0m Parse a document file.                                           [2m│[0m
[2m│[0m [1;36mread      [0m[1;36m [0m Read parsed document content by locator.                         [2m│[0m
[2m│[0m [1;36mscan      [0m[1;36m [0m Scan a file or directory into the document library.              [2m│[0m
[2m│[0m [1;36mwatch     [0m[1;36m [0m Manage directories watched for automatic scanning.               [2m│[0m
[2m│[0m [1;36msearch    [0m[1;36m [0m Search parsed document content.                                  [2m│[0m
[2m│[0m [1;36mfind      [0m[1;36m [0m Search filenames only (not document content).                    [2m│[0m
[2m│[0m [1;36musage     [0m[1;36m [0m Show remote parse service usage and limits.                      [2m│[0m
[2m│[0m [1;36mlist      [0m[1;36m [0m List document library resources.                                 [2m│[0m
[2m│[0m [1;36mshow      [0m[1;36m [0m Show document library resource details.                          [2m│[0m
[2m│[0m [1;36mtelemetry [0m[1;36m [0m Manage anonymous usage telemetry.                                [2m│[0m
[2m│[0m [1;36mserver    [0m[1;36m [0m Start, stop, and inspect the local MinerU server.                [2m│[0m
[2m│[0m [1;36mconfig    [0m[1;36m [0m Show or override MinerU configuration values.                    [2m│[0m
[2m│[0m [1;36minvalidate[0m[1;36m [0m Invalidate cached parse results so the next run parses again.    [2m│[0m
[2m│[0m [1;36mforget    [0m[1;36m [0m Remove file records and cached results from the document         [2m│[0m
[2m│[0m [1;36m           [0m library.                                                         [2m│[0m
[2m│[0m [1;36mcleanup   [0m[1;36m [0m Clean up local document library records and temp files.          [2m│[0m
[2m│[0m [1;36mversion   [0m[1;36m [0m Print MinerU and Python versions.                                [2m│[0m
[2m╰──────────────────────────────────────────────────────────────────────────────╯[0m

```

## install tail
```
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:42.74
	Maximum resident set size (kbytes): 308336
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
```
