import os
from pathlib import Path

ROOT = Path(r"C:\Users\user\Desktop\University\Other\Racing\cones_data\cones_data\cones_dataset")

IMG_DIR = ROOT / "images"
LBL_DIR = ROOT / "labels"

img_exts = {".jpg", ".jpeg", ".png"}

images = [p for p in IMG_DIR.iterdir() if p.suffix.lower() in img_exts]
print("Images found:", len(images))

missing_labels = []
bad_lines = []

for img_path in images:
    lbl_path = LBL_DIR / (img_path.stem + ".txt")

    if not lbl_path.exists():
        missing_labels.append(img_path.name)
        continue

    with open(lbl_path, "r") as f:
        lines = [ln.strip() for ln in f.readlines() if ln.strip()]

    for i, line in enumerate(lines, start=1):
        parts = line.split()
        if len(parts) != 5:
            bad_lines.append((lbl_path.name, i, "Not 5 values", line))
            continue

        try:
            cls = int(float(parts[0]))
            xc, yc, w, h = map(float, parts[1:])
        except:
            bad_lines.append((lbl_path.name, i, "Not numbers", line))
            continue

        for val, name in [(xc,"xc"), (yc,"yc"), (w,"w"), (h,"h")]:
            if not (0.0 <= val <= 1.0):
                bad_lines.append((lbl_path.name, i, f"{name} out of [0,1]", line))

print("\n--- RESULTS ---")
print("Missing label files:", len(missing_labels))
if missing_labels[:10]:
    print("Example missing:", missing_labels[:10])

print("Bad label lines:", len(bad_lines))
if bad_lines[:10]:
    print("\nExamples of bad lines:")
    for item in bad_lines[:10]:
        print(item)