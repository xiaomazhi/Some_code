import os
import xml.etree.ElementTree as ET
def xyxy2xywh(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2 * dw
    y = (box[1] + box[3]) / 2 * dh
    w = (box[2] - box[0]) * dw
    h = (box[3] - box[1]) * dh
    return (x, y, w, h)
def voc2yolo(path,classes,outpath):
    print(len(os.listdir(path)))
    for file in os.listdir(path):
        label_file = path + file
        out_file = open(outpath + '/'+file.replace('xml', 'txt'), 'w')
        tree = ET.parse(label_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        for obj in root.iter('object'):

            # difficult = obj.find('difficult').text
            cls = obj.find('name').text
            # if cls not in classes or int(difficult) == 1:
            #     continue
            cls_id = classes.index(cls)
            bndbox = obj.find('bndbox')
            box = [float(bndbox.find('xmin').text), float(bndbox.find('ymin').text), float(bndbox.find('xmax').text),
                float(bndbox.find('ymax').text)]
            bbox = xyxy2xywh((w, h), box)
            out_file.write(str(cls_id) + " " + " ".join(str(x) for x in bbox) + '\n')

# 定义类别列表
class_list = ["A2", "A10", "A3", "A19", "A1", "A13", "A20", "A15", "A16", "A17", "A12", "A5", "A14", "A7", "A9", "A4", "A18",
         "A8", "A11", "A6"]  # 根据需要替换类别名称

# VOC标签文件夹路径
voc_labels_path = '/root/mms/yolov10/data/VOCdevkit/VOC2007/Annotations/'

# YOLO标签文件夹路径
yolo_labels_path = '/root/mms/yolov10/data/VOCdevkit/yolo_all_txt'

# 调用函数进行转换
voc2yolo(voc_labels_path, class_list, yolo_labels_path)
