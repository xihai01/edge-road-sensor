import glob, os

root = "data/raw/crack500/CRACK500"

def sources(folder):
    stems = {os.path.splitext(os.path.basename(f))[0]
             for f in glob.glob(f"{root}/{folder}/*.png")}
    return {s.rsplit("_", 2)[0] for s in stems}  # strip row/col offsets

splits = {name: sources(name) for name in ["traincrop", "valcrop", "testcrop"]}
for name, src in splits.items():
    print(f"{name}: {len(src)} source photos")

names = list(splits)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        shared = splits[names[i]] & splits[names[j]]
        print(f"{names[i]} & {names[j]}: {len(shared)} shared", sorted(shared)[:5])