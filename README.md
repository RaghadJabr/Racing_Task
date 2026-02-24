# Racing_Task
# 🏎 Racing Task – Cone Detection System

This project implements an object detection system for detecting racing cones using deep learning models (RT-DETR / YOLO).  
The system is trained on a custom dataset and supports both image and video inference.

---

## 📌 Project Description

The objective of this project is to:

- Train an object detection model to detect racing cones
- Split dataset into training and validation sets
- Evaluate model performance
- Run inference on images and videos
- Save prediction outputs and metrics

This project demonstrates end-to-end deep learning workflow:
dataset preparation → training → evaluation → deployment.


---

## ⚙ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/RaghadJabr/Racing_Task.git
cd Racing_Task
Install Git LFS (Required for large files)
git lfs install
git lfs pull

This will download the large .pt model weights and video files.

3️⃣ Install Python dependencies
pip install -r requirements.txt

Recommended:

Python 3.10+

GPU support (CUDA) for training

🏋 Training the Model

To train the RT-DETR model:

python train_rtdetr.py

Training parameters:

Image size: 640

Batch size: 4

Epochs: 30

Device: GPU (if available)

Results will be saved in:

runs/detect/train*
🧪 Testing the Model

To evaluate on test images:

python test_rtdetr.py
🎥 Running Video Inference

To detect cones in a video:

python video_test.py

Output videos are saved inside:

runs/detect/predict*
📊 Outputs

The project generates:

Loss curves

Precision / Recall

mAP scores

Predicted images

Processed videos with bounding boxes

All outputs are stored inside:

runs/detect/
🧠 Models Used

RT-DETR (Real-Time Detection Transformer)

YOLO lightweight model

The dataset is structured in YOLO format with bounding box annotations.

📦 Dependencies

Main libraries used:

torch

ultralytics

opencv-python

numpy

matplotlib

Install all dependencies using:

pip install -r requirements.txt

