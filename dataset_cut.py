import os
import random

xmlfilepath = 'F:/dataset/HRSC2016_dataset/HRSC2016/HRSC2016/FullDataSet/Annotations'

saveBasePath = 'F:/dataset/new/'

trainval_percent = 0.66
train_percent = 0.66
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

print("train and val size", tv)
print("traub suze", tr)
ftrainval = open(os.path.join(saveBasePath, 'trainval1.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test1.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train1.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val1.txt'), 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()