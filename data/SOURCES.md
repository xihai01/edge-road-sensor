# Data sources

## RDD2022
- Source: https://github.com/sekilab/RoadDamageDetector (figshare DOI 10.6084/m9.figshare.21431547.v1)
- Downloaded: 2026-11-12
- Subsets: Japan, India, Czech, Norway, United_States, China_MotorBike, China_Drone
- Licence: <copy exactly from the figshare page>
- Checksums: data/raw/rdd2022/SHA256SUMS.txt
- Citation: Arya et al., "RDD2022: A multi-national image dataset for automatic road damage detection," 2022.
- Notes: Only train folders are labelled. China_Drone is aerial; decision on inclusion: <pending>.

## CRACK500
- Source: https://github.com/fyangneil/pavement-crack-detection (Google Drive / OneDrive link in README)
- Downloaded: 2026-11-12
- Version: <full images or ~3,368 patches; note which>
- Licence: <as stated at source; if none stated, write "none stated" and confirm research use with supervisor>
- Checksums: data/raw/crack500/SHA256SUMS.txt
- Citation: Yang et al., "Feature pyramid and hierarchical boosting network for pavement crack detection," IEEE T-ITS, 2020; Zhang et al., ICIP 2016.
- Notes: pixel masks (crack = 255); converted to boxes in Month 2. Patches grouped by source image when splitting.
- Split: official split not used. It places bursts of near-identical photos (taken seconds apart)
  in different splits; 6 photos appear in two splits outright. Re-split by burst: photos within
  30 s of each other grouped (visually confirmed at 5 s), whole groups assigned 70/15/15,
  seed <N>. Assignment: configs/crack500_split.csv (183 groups, 442 photos, 3,368 crops).

  ## COCO 2017 (vehicle subset)
- Source: https://cocodataset.org (annotations_trainval2017.zip; images fetched individually via coco_url)
- Downloaded: 2026-11-16
- Filter: images with >= 1 non-crowd car/bus/truck box covering >= 0.5% of the image;
  all vehicle labels in kept images retained. Script: src/fetch_coco_vehicles.py
- Image IDs: configs/coco_vehicle_ids_train2017.txt, configs/coco_vehicle_ids_val2017.txt
- Licence: <copy from cocodataset.org terms of use; annotations and images have separate terms>
- Citation: Lin et al., "Microsoft COCO: Common objects in context," ECCV 2014.
- Notes: still images, no track IDs; used for vehicle detection only, not MOTA.

## UA-DETRAC
- Source: <mirror used — official site detrac-db.rit.albany.edu was unavailable/not used>
- Downloaded: 2026-11-16
- Contents: 100 sequences (60 train / 40 test), 8,289 tracks, 1,274,055 boxes; verified against
  Wen et al. (~8,250 vehicles, ~1.21M boxes). No missing frames.
- Licence: <as stated at source>
- Citation: Wen et al., "UA-DETRAC: A new benchmark and protocol for multi-object detection
  and tracking," CVIU, 2020.
- Notes: split by sequence only (official split kept for MOTA/IDF1 comparability).
  Trucks nearly absent (74 "others" tracks); van -> Car mapping pending.