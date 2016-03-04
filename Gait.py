'''
@file    : Gait.py
@time    : Feb 26,2016 10:16
@author  : duanxxnj@163.com
'''

import numpy as np


class Gait:

    def __init__(self, gaitImageFrame):

        self.widthVector = []
        self.widthVectorLeft = []
        self.widthVectorRight = []
        self._heightStart = 0
        self._heightEnd = 0
        self._height = 0.0
        self._gaitImageFrame = gaitImageFrame.copy()


        self.extractGaitHight()


    def extractWidthVector(self):
        """

        :return:
        """

    @property
    def heihgt(self):
        return self._height

    def extractGaitHight(self):
        verticalSum = np.sum(self._gaitImageFrame, 1)
        verticalLen = len(verticalSum)

        for index in range(verticalLen):
            if verticalSum[index] > 0:
                self._heightStart = index
                break

        for index in range(verticalLen):
            if verticalSum[verticalLen - index - 1]:
                self._heightEnd = verticalLen - index - 1
                break

        self._height = self._heightEnd - self._heightStart
