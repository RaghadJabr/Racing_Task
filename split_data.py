import random, shutil
from pathlib import Path

root = Path(r"C:\Users\user\Desktop\University\Other\Racing\cones_data\cones_data\cones_dataset")
img_dir = root / "images"
lbl_dir = root / "labels"

images = list(img_dir.glob("*.jpg")) + list(img_dir.glob("*.png")) + list(img_dir.glob("*.jpeg"))

random.seed(42)
random.shuffle(images)

split = int(0.8 * len(images))
train_imgs = images[:split]
val_imgs = images[split:]

(img_dir / "train").mkdir(parents=True, exist_ok=True)
(img_dir / "val").mkdir(parents=True, exist_ok=True)
(lbl_dir / "train").mkdir(parents=True, exist_ok=True)
(lbl_dir / "val").mkdir(parents=True, exist_ok=True)

def move_pair(img_path: Path, split_name: str):
    shutil.move(str(img_path), str(img_dir / split_name / img_path.name))

    label_path = lbl_dir / f"{img_path.stem}.txt"
    if label_path.exists():
        shutil.move(str(label_path), str(lbl_dir / split_name / label_path.name))
    else:
        print("Missing label for:", img_path.name)

for p in train_imgs:
    move_pair(p, "train")

for p in val_imgs:
    move_pair(p, "val")

print("Train images:", len(train_imgs))
print("Val images:", len(val_imgs))