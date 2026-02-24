from ultralytics import RTDETR

def main():
    model = RTDETR("rtdetr-l.pt")
    model.train(
        data=r"C:\Users\user\Desktop\University\Other\Racing\cones_data\cones_data\cones_dataset\config.yaml",
        imgsz=640,
        epochs=30,
        batch=4,
        workers=4,
        device=0
    )

if __name__ == "__main__":
    main()