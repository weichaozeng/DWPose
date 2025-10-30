#!/bin/bash
pip install -r requirements.txt
pip install -U openmim
echo "Installing MMLab dependencies via mim..."
mim install mmengine "mmcv>=2.0.1" "mmdet>=3.1.0" "mmpose>=1.1.0"
echo "Installation complete for DWPose."