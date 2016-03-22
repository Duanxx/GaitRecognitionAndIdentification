'''
@file    : GaitIdentificationWithDTW.py
@time    : Mar 05,2016 09:59
@author  : duanxxnj@163.com
'''

from GaitDataSet import GaitDataSet
from matplotlib import pyplot as plt

from scipy.signal import argrelmin
from scipy.signal import find_peaks_cwt

import numpy as np

from dtw import dtwGaitSeq
from sklearn.metrics.pairwise import euclidean_distances

from GaitStepSeqFilter import GaitStepSeqFilter


import cv2

gds = GaitDataSet()

gaitDataSetFilePath = '/home/Duanxx/Documents/GraduateDesign/gait_dataset/CASIA/DatasetB/silhouettes'

gds.loadDataSet(gaitDataSetFilePath, loadNum=2)

print 'DataSet Load Ok'

dataSetLen = len(gds.data)

print dataSetLen

distanceMatrix = []

"""
    TO DO
        smooth of step sequence
        find the peaks of smoothed step sequence
        align the gait width sequence with the peaks in DTW
"""

gssf = GaitStepSeqFilter()

plt.figure(1)

plt.plot(range(len(gds.data[0].stepSeq)),
         gds.data[0].stepSeq,
         color='g')

plt.plot(range(len(gds.data[0].stepSeq)),
         gssf.smooth(np.array(gds.data[0].stepSeq), window_len=6),
         color='b')

plt.scatter(range(len(gds.data[0].stepSeq)),
            gds.data[0].stepSeq,
            color='r')

plt.scatter(range(len(gds.data[0].stepSeq)),
            gssf.smooth(np.array(gds.data[0].stepSeq), window_len=6),
            color='k')


peakind = find_peaks_cwt(gssf.smooth(np.array(gds.data[0].stepSeq),
                                     window_len=6),
                         np.arange(1, 4))

plt.show()


print argrelmin(np.array(gds.data[0].stepSeq))


for testIndex in range(0, dataSetLen, 2):
    row = []

    for trainIndex in range(1, dataSetLen, 2):
        print testIndex, trainIndex
        row.append(dtwGaitSeq(gds.data[testIndex],
                              gds.data[trainIndex],
                              euclidean_distances)[0])
    distanceMatrix.append(row)

print np.argmin(distanceMatrix, 1)
