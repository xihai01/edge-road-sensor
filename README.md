# Edge Road Sensor

Multi-task road defect detection and vehicle tracking on a Jetson-class edge device.
Research plan: <link to revised ARP>

## Setup
1. Create env: `conda create -n roadsensor python=3.11`
2. Install PyTorch for your machine:
   - Mac: `pip install torch torchvision`
   - Linux (CUDA): command from pytorch.org for the workstation's CUDA version
   - Jetson: NVIDIA's Jetson PyTorch wheel for JetPack 6.0
3. `pip install -r requirements.txt`