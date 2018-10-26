# WIDER FACE PASCAL VOC ANNOTATIONS

This repository contains the [WIDER FACE](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/) annotations converted to the [Pascal VOC](http://host.robots.ox.ac.uk/pascal/VOC/) XML format.

Note, the convert.py is modified from [here](https://github.com/akofman/wider-face-pascal-voc-annotations) to:
1) Discard invalid bounding boxes (e.g. "0--Parade/0_Parade_Parade_0_452.jpg" x1 y1 w h: 0 0 0 0)
2) Added toprettyxml for xml readability

```
usage: convert.py [-h] [-ap ANNOTATIONS_PATH] [-tp TARGET_PATH]
                  [-ip IMAGES_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -ap ANNOTATIONS_PATH, --annotations-path ANNOTATIONS_PATH
                        the annotations file path.
                        ie:"./wider_face_split/wider_face_train_bbx_gt.txt".
  -tp TARGET_PATH, --target-path TARGET_PATH
                        the target directory path where XML files will be
                        copied.
  -ip IMAGES_PATH, --images-path IMAGES_PATH
                        the images directory path. ie:"./WIDER_train/images"
```

Convert wider annotation text files using the following commands:

```
$ ./convert.py -ap ./wider_face_split/wider_face_train_bbx_gt.txt -tp ./WIDER_train_annotations/ -ip ./WIDER_train/images/
$ ./convert.py -ap ./wider_face_split/wider_face_val_bbx_gt.txt -tp ./WIDER_val_annotations/ -ip ./WIDER_val/images/
```
