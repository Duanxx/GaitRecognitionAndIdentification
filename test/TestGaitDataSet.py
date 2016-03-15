'''
@file    : TestGaitDataSet.py
@time    : Mar 01,2016 10:03
@author  : duanxxnj@163.com
'''

from GaitDataSet import GaitDataSet
from matplotlib import pyplot as plt
import cv2

gds = GaitDataSet()

gaitDataSetFilePath = '/home/Duanxx/Documents/GraduateDesign/gait_dataset/CASIA/DatasetB/silhouettes'

gds.loadDataSet(gaitDataSetFilePath)

gds.findAllFiles()

print gds._numGaitSeq

for gait in gds.data[0].gaitSeq:
    plt.plot(gait.widthVector)

print len(gait.widthVector)

plt.show()
