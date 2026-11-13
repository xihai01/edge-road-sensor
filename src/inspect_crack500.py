import glob, os, collections
import cv2
import numpy as np

root = "data/raw/crack500"
imgs = {os.path.splitext(f)[0]: f for f in glob.glob(f"{root}/**/*", recursive=True)
        if f.lower().endswith(".jpg")}
masks = {os.path.splitext(f)[0]: f for f in glob.glob(f"{root}/**/*.png", recursive=True)}

print("images:", len(imgs), "| masks:", len(masks))
print("images without mask:", len(imgs.keys() - masks.keys()))
print("masks without image:", len(masks.keys() - imgs.keys()))

by_folder = collections.defaultdict(list)
for stem, path in masks.items():
    by_folder[os.path.dirname(path)].append(path)

for folder, paths in sorted(by_folder.items()):
    shapes, values, comps, empty = collections.Counter(), collections.Counter(), [], 0
    for p in paths:
        m = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
        shapes[m.shape] += 1
        values[tuple(np.unique(m)[:4])] += 1
        n, _ = cv2.connectedComponents((m > 127).astype(np.uint8))
        comps.append(n - 1)  # minus background
        empty += (n - 1) == 0
    print(f"\n{folder}: {len(paths)} masks")
    print("  shapes:", shapes.most_common(3))
    print("  pixel values:", values.most_common(3))
    print("  crack pieces per mask: median", np.median(comps), "| max", max(comps), "| empty masks", empty)