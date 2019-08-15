import os
import shutil
import numpy as np
import xml.etree.ElementTree as et
#import cv2
file_dir = 'F:\dataset\VOCtrainval_03-May-2010\VOCdevkit\VOC2010\Annotations'
file_it = 'F:\dataset\it.txt'
dstfile='F:/dataset/it'

def main():
    #tree = et.ElementTree
    f = open(file_it,'r')
    for i in open(file_it,'r'):
        for root, dirs, files in os.walk(file_dir):
            for j in files:
                if i[:-5] == j[:-4]:
                    srcfile = 'F:/dataset/VOCtrainval_03-May-2010/VOCdevkit/VOC2010/Annotations/%s.xml'%j[:-4]
                    print(srcfile)
                    shutil.move(srcfile, dstfile)
    f.close()

if __name__ == '__main__':
    main()