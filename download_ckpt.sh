#!/bin/bash

CKPTS_DIR="./ckpts"
DET_MODEL_URL="https://download.openmmlab.com/mmdetection/v2.0/yolox/yolox_l_8x8_300e_coco/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth"
POSE_MODEL_URL="https://huggingface.co/wanghaofan/dw-ll_ucoco_384/resolve/main/dw-ll_ucoco_384.pth"

echo "Creating directory: $CKPTS_DIR"
mkdir -p "$CKPTS_DIR"

echo "Downloading Detection Model (YOLOX)..."
wget -c "$DET_MODEL_URL" -O "$CKPTS_DIR/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth"

echo "Downloading Pose Model (dw-ll_ucoco_384)..."
wget -c "$POSE_MODEL_URL" -O "$CKPTS_DIR/dw-ll_ucoco_384.pth"
