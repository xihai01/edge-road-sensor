# Environment

Evidence for the Month 1 "environment setup confirmation" deliverable.
Each machine gets its own section: a short summary table, then the raw
output of the verify commands, pasted unedited.

Last updated: YYYY-MM-DD

## Summary

| Machine | Role | Status | Verified on |
| --- | --- | --- | --- |
| MacBook (Apple Silicon) | Development, data prep, smoke tests | Verified | 2026-11-04 |
| Linux GPU workstation | Model training | Pending school specs | — |
| Jetson (edge device) | Inference, power measurement | Pending hardware | — |

---

## 1. Mac (development)

| Item | Value |
| --- | --- |
| Model / chip | MacBook Pro, Apple M4 CPU |
| RAM | 32 GB |
| macOS | macOS-15.7.3-arm64-arm-64bit |
| Free disk at setup | 381.6/460.4 GB |
| Python env | conda `roadsensor`, Python 3.11.18 |
| PyTorch | 2.15.0 |
| Ultralytics | 8.4.202 |
| OpenCV / Supervision | 5.0.0, 0.31.4 |

### Verify output

Run on 2026-11-04.

```text
$ uname -m && sw_vers -productVersion
arm64
15.7.3

$ df -h ~
Filesystem      Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s5   460Gi   351Gi    79Gi    82%     10M  826M    1%   /System/Volumes/Data

$ python -c "import torch; print(torch.__version__, torch.backends.mps.is_available())"
2.15.0 True

$ yolo checks
Creating new Ultralytics Settings v0.0.8 file ✅
View Ultralytics Settings with 'yolo settings' or at '/Users/xihailuo/Library/Application Support/Ultralytics/settings.json'
Update Settings with 'yolo settings key=value', i.e. 'yolo settings runs_dir=path/to/dir'. For help see https://docs.ultralytics.com/usage/settings
Ultralytics 8.4.202 🚀 Python-3.11.18 torch-2.15.0 CPU (Apple M4)
Setup complete ✅ (10 CPUs, 32.0 GB RAM, 381.6/460.4 GB disk)

OS                     macOS-15.7.3-arm64-arm-64bit
Environment            Darwin
Python                 3.11.18
Install                pip
Path                   /opt/anaconda3/envs/roadsensor/lib/python3.11/site-packages/ultralytics
RAM                    32.00 GB
Disk                   381.6/460.4 GB
CPU                    Apple M4
CPU count              10
GPU                    None
GPU count              None
CUDA                   None

numpy                  ✅ 2.4.6>=1.23.0; platform_system != "Darwin"
numpy                  ✅ 2.4.6!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,!=2.3.1,!=2.3.2,!=2.3.3,!=2.3.4,>=1.23.0; platform_system == "Darwin"
matplotlib             ✅ 3.11.2>=3.3.0
opencv-python          ✅ 5.0.0.93!=4.13.0.90,>=4.7.0
pillow                 ✅ 13.0.0>=7.1.2
requests               ✅ 2.34.2>=2.23.0
torch                  ✅ 2.15.0>=1.8.0
torch                  ✅ 2.15.0!=2.4.0,>=1.8.0; sys_platform == "win32"
torchvision            ✅ 0.29.2>=0.9.0
psutil                 ✅ 7.2.2>=5.8.0
polars                 ✅ 2.1.0>=0.20.0
nvidia-ml-py           ✅ 13.615.71>=12.0.0
ultralytics-thop       ✅ 2.2.5>=2.2.4
ultralytics-platform   ✅ 0.1.102>=0.1.102; python_version >= "3.11"

$ python -c "import cv2, supervision; print(cv2.__version__, supervision.__version__)"
5.0.0 0.31.4
```

### Smoke test

`yolo train model=yolov8n.pt data=coco8.yaml epochs=1 imgsz=640 device=mps`

- Result: pass
- Epoch time: 1 rpoch in 0.002 hours
- Final mAP50 line (copy the last results row):

```text
Model summary (fused): 72 layers, 3,151,904 parameters, 0 gradients, 8.7 GFLOPs
                 Class     Images  Instances      Box(P       …: 100% ━━━━━━━━━━━━ 1/1 3.2it/s 0.3s
                   all          4         17      0.641      0.818      0.794      0.559
                person          3         10      0.803       0.41      0.535      0.274
                   dog          1          1      0.396          1      0.497      0.298
                 horse          1          2      0.901          1      0.995      0.746
              elephant          1          2       0.47        0.5      0.745      0.244
              umbrella          1          1      0.578          1      0.995      0.895
          potted plant          1          1      0.702          1      0.995      0.895
```

### Notes and deviations

- n/a

---

## 2. Linux GPU workstation (training)

Pending: waiting on the school to confirm GPU model, VRAM, OS and access method.

---

## 3. Jetson (edge)

Pending: hardware not yet received.

---

## 4. Repository & Tooling
```bash
(roadsensor) xihailuo@Mac edge-road-sensor % git remote -v && dvc --version && dvc remote list && mlflow --version
origin	git@github.com:xihai01/edge-road-sensor.git (fetch)
origin	git@github.com:xihai01/edge-road-sensor.git (push)
3.67.1
mlflow, version 3.18.0
```