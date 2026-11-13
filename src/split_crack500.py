import glob, os, csv, random, sys
from datetime import datetime

root = "data/raw/crack500/CRACK500"
GAP = int(sys.argv[1]) if len(sys.argv) > 1 else 30   # seconds
SEED, RATIOS = 42, {"train": 0.70, "val": 0.15, "test": 0.15}

crops = {}  # source photo -> number of crops
for split in ["traincrop", "valcrop", "testcrop"]:
    for f in glob.glob(f"{root}/{split}/*.png"):
        src = os.path.splitext(os.path.basename(f))[0].rsplit("_", 2)[0]
        crops[src] = crops.get(src, 0) + 1

def stamp(s):
    try:
        return datetime.strptime(s, "%Y%m%d_%H%M%S")
    except ValueError:
        return None

stamped = sorted((stamp(s), s) for s in crops if stamp(s))
groups, current, prev = [], [], None
for t, s in stamped:
    if prev and (t - prev).total_seconds() > GAP:
        groups.append(current)
        current = []
    current.append(s)
    prev = t
groups.append(current)
groups += [[s] for s in crops if not stamp(s)]  # IMG_xxxx photos: own group

size = lambda g: sum(crops[s] for s in g)
total = sum(crops.values())
print(f"gap {GAP}s: {len(groups)} groups from {len(crops)} photos, {total} crops")
print("largest groups (crops):", sorted(map(size, groups), reverse=True)[:5])

random.Random(SEED).shuffle(groups)
filled = dict.fromkeys(RATIOS, 0)
rows = []
for gid, g in enumerate(groups):
    split = max(RATIOS, key=lambda k: RATIOS[k] * total - filled[k])
    filled[split] += size(g)
    rows += [(s, split, gid) for s in g]
print("crop share:", {k: round(v / total, 3) for k, v in filled.items()})

with open("configs/crack500_split.csv", "w", newline="") as f:
    csv.writer(f).writerows([("photo", "split", "group")] + sorted(rows))