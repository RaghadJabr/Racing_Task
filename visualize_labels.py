import os, random
from pathlib import Path
import cv2
import matplotlib.pyplot as plt

ROOT = Path(r"C:\Users\user\Desktop\University\Other\Racing\cones_data\cones_data\cones_dataset")
IMG_DIR = ROOT / "images"
LBL_DIR = ROOT / "labels"
img_exts = [".jpg", ".jpeg", ".png"]

images = [p for p in IMG_DIR.iterdir() if p.suffix.lower() in img_exts]
img_path = random.choice(images)

lbl_path = LBL_DIR / (img_path.stem + ".txt")

img = cv2.cvtColor(cv2.imread(str(img_path)), cv2.COLOR_BGR2RGB)
H, W = img.shape[:2]

if lbl_path.exists():
    with open(lbl_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 5:
                continue
            cls, xc, yc, bw, bh = map(float, parts)
            x1 = int((xc - bw/2) * W)
            y1 = int((yc - bh/2) * H)
            x2 = int((xc + bw/2) * W)
            y2 = int((yc + bh/2) * H)
            cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,0), 2)
else:
    print("No label file for:", img_path.name)

plt.figure(figsize=(8,8))
plt.title(img_path.name)
plt.imshow(img)
plt.axis("off")
plt.show()