import glob, collections, xml.etree.ElementTree as ET

for country in sorted(glob.glob("data/raw/rdd2022/RDD2022/*/")):
    imgs = glob.glob(f"{country}train/**/*.jpg", recursive=True)
    xmls = glob.glob(f"{country}train/**/*.xml", recursive=True)
    classes, empty = collections.Counter(), 0
    for f in xmls:
        objs = list(ET.parse(f).getroot().iter("object"))
        empty += not objs
        for o in objs:
            classes[o.find("name").text] += 1
    print(country, len(imgs), "imgs |", len(xmls), "xml |", empty, "no-damage |", dict(classes))