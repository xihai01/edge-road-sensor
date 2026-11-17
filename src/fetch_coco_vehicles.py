import os, sys, concurrent.futures as cf, urllib.request
from pycocotools.coco import COCO

ROOT, MIN_FRAC, CLASSES = "data/raw/coco", 0.005, ["car", "bus", "truck"]
dry = "--dry-run" in sys.argv

for split in ["train2017", "val2017"]:
    coco = COCO(f"{ROOT}/annotations/instances_{split}.json")
    cats = coco.getCatIds(catNms=CLASSES)
    keep = set()
    for a in coco.loadAnns(coco.getAnnIds(catIds=cats, iscrowd=False)):
        img = coco.imgs[a["image_id"]]
        if a["bbox"][2] * a["bbox"][3] / (img["width"] * img["height"]) >= MIN_FRAC:
            keep.add(img["id"])
    counts = {coco.cats[c]["name"]: 0 for c in cats}
    for a in coco.loadAnns(coco.getAnnIds(imgIds=list(keep), catIds=cats)):
        counts[coco.cats[a["category_id"]]["name"]] += 1
    print(f"{split}: {len(keep)} images | vehicle instances: {counts}")

    with open(f"configs/coco_vehicle_ids_{split}.txt", "w") as f:
        f.write("\n".join(map(str, sorted(keep))) + "\n")
    if dry:
        continue

    out = f"{ROOT}/images/{split}"
    os.makedirs(out, exist_ok=True)
    def fetch(i):
        img = coco.imgs[i]
        dst = f"{out}/{img['file_name']}"
        if os.path.exists(dst):
            return "had"
        for _ in range(3):
            try:
                urllib.request.urlretrieve(img["coco_url"], dst + ".part")
                os.rename(dst + ".part", dst)
                return "new"
            except Exception:
                pass
        return "failed"
    with cf.ThreadPoolExecutor(8) as ex:
        res = list(ex.map(fetch, sorted(keep)))
    print(f"{split}: new {res.count('new')} | already had {res.count('had')} | failed {res.count('failed')}")