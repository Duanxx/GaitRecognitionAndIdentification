'''
@file    : Gait.py
@time    : Feb 26,2016 10:16
@author  : duanxxnj@163.com

the class Gait is defined in this file



'''

import numpy as np

import cv2

class Gait:
    """
    A Gait instance is the set of the features which extracted from particular
    gait image frame who is in binary model

    the features of a gait in detail:
        widthVector[] : the element in the vector is the difference between
        right bound and left bound for one row of a gait.the length of the
        widthVector is the row number of gait image frame

        centerRow, centerCol : the center of gait image in Row and Col
        respectively.

        widthVectorLeft[], widthVectorRight[] : the left and right widthVector
        from the centerRow

        step : the distance covered by a step

        height : the height of gait
    """

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
        self._gaitImageFrame = gaitImageFrame.copy()  # a copy of input gait

        # first get the height of a gait
        self.extractGaitHeight()

        # get the width vector
        self.extractWidthVector()

        # get the center of gait
        self.calcCenter()

        self._gaitImageFrame = []

    @property
    def height(self):
        return self._height

    def extractWidthVector(self):
        """
            for each row of gait, find the first and last nonzero point index
            calculate the difference between last and first nonzero point index
            all the difference construct the widthVector[]
        :return:
        """

        for row in self._gaitImageFrame:
            startIndex, endIndex = self.findFirstAndLastNonZeroValueIndex(row)
            self.widthVector.append(endIndex - startIndex)

        # only take the 1/4 lower part of the gait into consideration
        # the maximum widthVector who is in consideration is the step
        # force convert to int, save the memory
        self.step = int(np.amax(self.widthVector[
                                 self._heightEnd - int(self._height/4):
                                 self._heightEnd]))

    def extractGaitHeight(self):
        """
            the height of a gait.
        :return:
        """

        # the sum of gait image frame in dimension 1, which is the sum of
        # columns in row. for example :
        # In : a = [[1, 2], [1, 2], [1, 2]]
        # In : np.sum(a, 1)
        # out: array([3, 3, 3])
        verticalSum = np.sum(self._gaitImageFrame, 1)

        # the difference of last pint and first nonzero point in vertical is
        # the height
        self._heightStart, self._heightEnd = \
            self.findFirstAndLastNonZeroValueIndex(verticalSum)
        self._height = self._heightEnd - self._heightStart

    def findFirstAndLastNonZeroValueIndex(self, inputList):
        """
            for a inputList, find the first and last nonzero point
        :param inputList:
        :return:
        """

        inputLen = len(inputList)

        # if inputList is empty raise
        if inputLen == 0:
            raise ValueError(' the input list is empty ')

        startIndex = 0  # the start pixel index of nonzero point
        endIndex = 0  # the end pixel index of nonzero point

        inputListCopy = inputList.copy()  # a copy of input list

        # find the first nonzero point in inputList
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

    def calcCenter(self):
        """
            the center of gait image
        :return:
        """
        gaitmoment = cv2.moments(self._gaitImageFrame)

        self.centerRow = int(gaitmoment['m01']/gaitmoment['m00'])
        self.centerCol = int(gaitmoment['m10']/gaitmoment['m00'])