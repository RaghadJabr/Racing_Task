from ultralytics import RTDETR

model = RTDETR(r"C:\Users\user\Desktop\University\Other\Racing\cones_data\runs\detect\train5\weights\best.pt") 

model.predict(
    source=r"C:\Users\user\Desktop\University\Other\Racing\AD.mp4", 
    imgsz=640,
    device=0,
    save=True,
    conf=0.25
)

print("Video detection complete!")