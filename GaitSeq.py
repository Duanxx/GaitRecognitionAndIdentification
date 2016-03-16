'''
@file    : GaitSeq.py
@time    : Feb 26,2016 10:14
@author  : duanxxnj@163.com
'''

import os
import cv2
import numpy as np

from Gait import Gait
from GaitStepSeqFilter import GaitStepSeqFilter

class GaitSeq():

    def __init__(self, gaitSeqFilePath,showImage=False):
        """

        :return:
        """

        self._gaitSeqFilePath = gaitSeqFilePath
        self._gaitIndex = []

        self.gaitSeq = []
        self.stepSeq = []
        self.stepSeqSmoothed = []
        self.standAndStraddle = []

        self.gaitSeqID = ''
        self.gaitSeqWear = ''
        self.gaitSeqWearID = ''
        self.gaitSeqAngle = ''

        self.loadGaitSeq(showImage)
        self.loadStepSeq()
        self.loadStepSeqSmoothed()

    def information(self):
        print 'gaitSeqID = \t', self.gaitSeqID
        print 'gaitSeqWear = \t', self.gaitSeqWear
        print 'gaitSeqWearID = ', self.gaitSeqWearID
        print 'gaitSeqAngle = \t', self.gaitSeqAngle
        print

    def extractGaitSeqProfile(self, GaitSeqRootFilePath):

        self.gaitSeqID = GaitSeqRootFilePath.split('/')[-3]
        self.gaitSeqWear = GaitSeqRootFilePath.split('/')[-2].split('-')[0]
        self.gaitSeqWearID = GaitSeqRootFilePath.split('/')[-2].split('-')[1]
        self.gaitSeqAngle = GaitSeqRootFilePath.split('/')[-1]

    def loadGaitSeq(self, showImage=False):
        """
            get the file path of gait sequence
        :return: gaitFilePath []
        """
        for root, dirs, files in os.walk(self._gaitSeqFilePath):

            # get the basic profiles of gait sequence
            self.extractGaitSeqProfile(root)

            # as the files read are not in index
            # so sort the files in ascending
            for file in files:
                self._gaitIndex.append(file[-7:-4])
            self._gaitIndex.sort()

            for file, index in zip(files, self._gaitIndex):
                filePath = root + '/' + file[:-7] + index + file[-4:]

                if os.path.isfile(filePath):
                    # read image in graysacle
                    gaitFrame = cv2.imread(filePath, 0)

                    # if file is broken
                    if not isinstance(gaitFrame, np.ndarray):
                        print filePath, ' is broken'
                        break

                    # binary image
                    ret, gaitFrameBinary = cv2.threshold(gaitFrame,
                                                   100,
                                                   1,
                                                   cv2.THRESH_BINARY)

                    if showImage:
                        cv2.imshow('duanxx', gaitFrame)
                        cv2.waitKey(1)

                    self.gaitSeq.append(Gait(gaitFrameBinary))

    def loadStepSeq(self):

        for gait in self.gaitSeq:
            self.stepSeq.append(gait.step)

    def loadStepSeqSmoothed(self):
        gssf = GaitStepSeqFilter()

        if len(self.stepSeq) < 1:
            raise Exception('the length of stepSeq is less than 1')
        else:
            self.stepSeqSmoothed = gssf.smooth(np.array(self.stepSeq))

    def findGaitSeqPeaks(self):
        pass