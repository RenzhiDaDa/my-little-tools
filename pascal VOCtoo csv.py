#!/usr/bin/evn python
'''
this code is for pascal voc to retinanet
and the code is completed with python3
it is used for .xml to txt
'''
# coding:utf-8
import os
import glob

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

filename = glob.glob('F:/dataset/HRSC2016_dataset/HRSC2016/HRSC2016/FullDataSet/Annotations/' + '*xml')
fileObject = open('F:/dataset/new/test1.txt', 'w')

for ip in filename:
    fileObject.write(ip)
    fileObject.write('\n')
fileObject.close()

file_srx = open("F:/dataset/new/test1.txt")  # 其中包含所有待计算的文件名
line = file_srx.readline()
while line:
    f = line[:-1]  # 除去末尾的换行符
    tree = ET.parse(f)  # 打开xml文档
    root = tree.getroot()  # 获得root节点
    print("*" * 10)
    filename = root.find('Img_ID').text
    #filename = filename[:-8]
    print(filename)
    dir_name = 'F:/dataset/new/txt'
    if os.path.exists(dir_name) == False:
        os.mkdir(dir_name)
        
        # file_object_txt = open(dir_name +'/' + filename + ".txt","a")
    # # file_object_txt = open(dir_name, 'w') #写文件
    # file_object_txt.write(filename +'\t')
    
    # file_object_log = open(filename + ".log", 'w') #写文件
    flag = False
    '''
    ########################################
    
    for size in root.findall('./HRSC_Objects/HRSC_Object'):  # 找到root节点下的size节点
        width = size.find('width').text  # 子节点下节点width的值
        height = size.find('height').text  # 子节点下节点height的值
        print (width, height)
    ########################################
    '''
    file_object_txt = open(dir_name + '/' + 'test' + ".txt", "a")
    for objects in root.findall('./HRSC_Objects'):  # 找到root节点下的所有object节点
        #bndbox = object.find('bndbox')  # 子节点下属性bndbox的值
        filename = root.find('Img_ID').text
        #file_object_txt = open(dir_name + '/' + filename + ".txt", "a")
        file_object_txt.write(filename + '.jpg' + '\t')
        num=0
        for object in objects.findall('./HRSC_Object'):
            num+=1
            print(num)
            xmin = object.find('box_xmin').text
            ymin = object.find('box_ymin').text
            xmax = object.find('box_xmax').text
            ymax = object.find('box_ymax').text
            file_object_txt.write(xmin + '\t' + ymin + '\t' + xmax + '\t' + ymax + '\t')
            print(xmin, ymin, xmax, ymax)
            classname = object.find('Class_ID').text
            class_name = classname[7:]
            print(type(classname))
            if classname:
                file_object_txt.write('0' + '\t')
        file_object_txt.write('\n')
        '''
        if class_name in ['01','02','03','04','05','06','07','08','09']:
            file_object_txt.write(classname[8:] + '\n')
        else:
            file_object_txt.write(classname[7:] + '\n')
        '''
        #file_object_txt.write(classname[8:] + '\n')
        #print(classname[7:])
    file_object_txt.close()
    # file_object_log.close()
    if flag == False:  # 如果没有符合条件的信息，则删掉相应的txt文件以及jpg文件
        # os.remove(filename + ".txt")
        # os.remove(filename + ".jpg")
        # os.remove(filename + ".log")
        pass
    line = file_srx.readline()
