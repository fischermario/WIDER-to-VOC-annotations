# WIDER FACE PASCAL VOC ANNOTATIONS

This repository contains the [WIDER FACE](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/) annotations converted to the [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/) XML format.

```
usage: convert.py [-h] [-ap ANNOTATIONS_PATH] [-td TARGET_PATH]
                  [-id IMAGES_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -ap ANNOTATIONS_PATH, --annotations-path ANNOTATIONS_PATH
                        the annotations file path.
                        ie:"./wider_face_split/wider_face_train_bbx_gt.txt".
  -td TARGET_DIR,       --target-dir TARGET_DIR
                        the target directory where XML files will be saved.
  -id IMAGES_DIR,       --images-dir IMAGES_DIR
                        the images directory. ie:"./WIDER_train/images"
```

Convert wider annotation text files using the following commands:

```
$ ./convert.py -ap ./wider_face_split/wider_face_train_bbx_gt.txt -td ./WIDER_train_annotations/ -id ./WIDER_train/images/
$ ./convert.py -ap ./wider_face_split/wider_face_val_bbx_gt.txt -td ./WIDER_val_annotations/ -id ./WIDER_val/images/
```

Note: the convert.py is modified from [here](https://github.com/akofman/wider-face-pascal-voc-annotations) to:
1) Discard invalid bounding boxes (e.g. "0--Parade/0_Parade_Parade_0_452.jpg" x1 y1 w h: 0 0 0 0)
2) Add toprettyxml for xml readability
