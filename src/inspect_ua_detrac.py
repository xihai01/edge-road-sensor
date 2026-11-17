import glob, os, collections
import xml.etree.ElementTree as ET

root = "data/raw/ua-detrac"
xmls = sorted(glob.glob(f"{root}/**/*.xml", recursive=True))
img_dirs = {os.path.basename(d): d for d in glob.glob(f"{root}/**/MVI_*", recursive=True)
            if os.path.isdir(d)}
print(len(xmls), "XML files |", len(img_dirs), "image folders")

by_folder = collections.defaultdict(list)
for x in xmls:
    by_folder[os.path.dirname(x)].append(x)

for folder, files in sorted(by_folder.items()):
    track_types, frames, boxes, short = collections.Counter(), 0, 0, []
    for x in files:
        r = ET.parse(x).getroot()
        seq, fr = r.get("name"), r.findall("frame")
        frames += len(fr)
        ids = {}
        for f in fr:
            for t in f.iter("target"):
                boxes += 1
                ids[t.get("id")] = t.find("attribute").get("vehicle_type")
        track_types.update(ids.values())
        n_imgs = len(glob.glob(f"{img_dirs[seq]}/*.jpg")) if seq in img_dirs else 0
        if n_imgs < len(fr):
            short.append((seq, n_imgs, len(fr)))
    print(f"\n{folder}: {len(files)} sequences | {frames} annotated frames | "
          f"{sum(track_types.values())} tracks | {boxes} boxes")
    print("  tracks by vehicle type:", dict(track_types))
    print("  sequences missing images:", len(short), short[:3])