'''
@file    : TestGaitDataSet.py
@time    : Mar 01,2016 10:03
@author  : duanxxnj@163.com
'''

from GaitDataSet import GaitDataSet

import cv2

gds = GaitDataSet()

gaitDataSetFilePath = '/home/Duanxx/Documents/GraduateDesign/gait_dataset/CASIA/DatasetB/silhouettes'

gds.loadDataSet(gaitDataSetFilePath)

gds.findAllFiles()

print gds._numGaitSeq

for index in xrange(100):
    print gds.data[index]._gaitIndex

cv2.imshow('duanxx', gds.data[0].gaitSeq[0]._gaitImageFrame)
cv2.waitKey()