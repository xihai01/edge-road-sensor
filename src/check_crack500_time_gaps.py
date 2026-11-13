import glob, os
from datetime import datetime

root = "data/raw/crack500/CRACK500"
photos = {}  # source photo -> split
for split in ["traincrop", "valcrop", "testcrop"]:
    for f in glob.glob(f"{root}/{split}/*.png"):
        src = os.path.splitext(os.path.basename(f))[0].rsplit("_", 2)[0]
        photos.setdefault(src, set()).add(split)

stamped = {}
for src, splits in photos.items():
    try:
        stamped[src] = (datetime.strptime(src, "%Y%m%d_%H%M%S"), splits)
    except ValueError:
        pass  # non-timestamp names like IMG_2915

print(f"{len(stamped)} of {len(photos)} photos have timestamp names")
items = sorted(stamped.items(), key=lambda kv: kv[1][0])
for gap in [5, 30, 120]:
    pairs = [(a, b) for (a, (ta, sa)), (b, (tb, sb)) in zip(items, items[1:])
             if (tb - ta).total_seconds() <= gap and sa != sb]
    print(f"within {gap:>3}s, different splits: {len(pairs)}", pairs[:4])