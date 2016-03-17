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
        self.step = 0.0
        self.centerRow = 0
        self.centerCol = 0
        self._gaitImageFrame = gaitImageFrame.copy()

        self.extractGaitHight()

        self.extractWidthVector()

        self.calcCenterXY()

        self._gaitImageFrame = []

    @property
    def height(self):
        return self._height

    def extractWidthVector(self):

        for row in self._gaitImageFrame:

            startIndex, endIndex = self.findFirstAndLastNotZeroValueIndex(row)
            self.widthVector.append(endIndex - startIndex)

        # force convert to int, save the memory
        self.step = int(np.amax(self.widthVector[
                                 self._heightEnd - int(self._height/4):
                                 self._heightEnd]))

    def extractGaitHight(self):
        verticalSum = np.sum(self._gaitImageFrame, 1)
        
        self._heightStart, self._heightEnd = \
            self.findFirstAndLastNotZeroValueIndex(verticalSum)

        self._height = self._heightEnd - self._heightStart


    def findFirstAndLastNotZeroValueIndex(self, inputList):
        inputLen = len(inputList)

        startIndex = 0
        endIndex = 0

        # if inputList is empty return directly
        if inputLen == 0:
            return startIndex, endIndex

        inputListCopy = inputList.copy()

        # find the first not zero point in inputList
        for index in range(inputLen):
            if inputListCopy[index] > 0:
                startIndex = index
                break

        # find the last not zero point in inputList
        for index in range(inputLen):
            if inputListCopy[inputLen - index - 1] > 0:
                endIndex = inputLen - index - 1
                break

        return startIndex, endIndex

    def calcCenterXY(self):

        ImageFrameSize = self._gaitImageFrame.shape

        for rowindex in range(ImageFrameSize[0]):
            for colindex in range(ImageFrameSize[1]):
                """
                    TO DO centerRow and centerCOl
                """
