from ultralytics import RTDETR
from pathlib import Path

model = RTDETR(r"C:\Users\user\Desktop\University\Other\Racing\cones_data\runs\detect\train5\weights\best.pt") 

source = Path(r"C:\Users\user\Desktop\University\Other\Racing\cones_data\cones_data\cones_dataset\images\val")
model.predict(source=str(source), imgsz=640, conf=0.25, save=True)