import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from PIL import Image
import os
import argparse
import sys

def createAnnotationPascalVocTree(folder, basename, path, width, height):
    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = basename
    #ET.SubElement(annotation, 'path').text = path

    source = ET.SubElement(annotation, 'source')
    ET.SubElement(source, 'database').text = 'Unknown'

    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = '3'

    ET.SubElement(annotation, 'segmented').text = '0'

    return ET.ElementTree(annotation)

def createObjectPascalVocTree(xmin, ymin, xmax, ymax, image_width, image_height):
    obj = ET.Element('object')
    ET.SubElement(obj, 'name').text = 'face'
    ET.SubElement(obj, 'pose').text = 'Unspecified'
    ET.SubElement(obj, 'truncated').text = '0'
    ET.SubElement(obj, 'difficult').text = '0'

    bndbox = ET.SubElement(obj, 'bndbox')
    ET.SubElement(bndbox, 'xmin').text = str(max(xmin,0))
    ET.SubElement(bndbox, 'ymin').text = str(max(ymin,0))
    ET.SubElement(bndbox, 'xmax').text = str(min(xmax,image_width))
    ET.SubElement(bndbox, 'ymax').text = str(min(ymax,image_height))

    return ET.ElementTree(obj)

def parseImFilename(imFilename, imPath):
    im = Image.open(os.path.join(imPath, imFilename))
            
    folder, basename = imFilename.split('/')
    width, height = im.size

    return folder, basename, imFilename, width, height

def convertWFAnnotations(annotationsPath, targetPath, imPath):
    ann = None
    basename = ''
    with open(annotationsPath) as f:
        line = f.readline().strip()
        while line:
            imFilename = line
            folder, basename, path, width, height = parseImFilename(imFilename, imPath)
            ann = createAnnotationPascalVocTree(folder, basename, os.path.join(imPath, path), width, height)
            nbBndboxes = f.readline().strip()
            
            i = 0
            while i < int(nbBndboxes):
                i = i + 1
                x1, y1, w, h, _, _, _, _, _, _ = [int(k) for k in f.readline().split()]
                x2 = x1 + w
                y2 = y1 + h

                if (x2 <= x1 or y2 <= y1):
                    print('Error Image "{}" x1 y1 w h: {} {} {} {}'.format(imFilename,x1,y1,w,h))
                    continue

                ann.getroot().append(createObjectPascalVocTree(x1, y1, x2, y2, width, height).getroot())

            xmlstr = minidom.parseString(ET.tostring(ann.getroot())).childNodes[0].toprettyxml(indent="    ")
            if not os.path.exists(targetPath):
                 os.makedirs(targetPath)
            annFilename = os.path.join(targetPath, basename.replace('.jpg','.xml'))
            with open(annFilename,"w") as sf:
                sf.write(xmlstr)
            print('{} => {}'.format(basename, annFilename))
            line = f.readline().strip()

def parse_args():
    parser = argparse.ArgumentParser(description='Convert WIDER annotations to VOC format')
    parser.add_argument('-ap', dest='annotations_path', help='the annotations file path. ie:"./wider_face_split/wider_face_train_bbx_gt.txt".')
    parser.add_argument('-tp', dest='target_path', help='the target directory path where XML files will be copied.')
    parser.add_argument('-ip', dest='images_path', help='the images directory path. ie:"./WIDER_train/images"')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse_args()
    
    convertWFAnnotations(args.annotations_path, args.target_path, args.images_path)

