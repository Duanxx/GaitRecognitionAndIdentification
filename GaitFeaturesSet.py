'''
@file    : GaitFeaturesSet.py
@time    : Mar 15,2016 16:35
@author  : duanxxnj@163.com
'''

import os
import csv
import numpy as np

import matplotlib.pyplot as plt

class GaitFeaturesSet:

    def __init__(self):
        self._FeaturesSetPath = ""
        self._gaitFeaturesSetFilePath = ""
        self.gaitWidthVectors = []
        self.gaitWidthVectorsLeft = []
        self.gaitWidthVectorsRight = []
        self.gaitStepSeqs = []
        pass

    def loadFeaturesSet(self, FeaturesSetFilePath, gaitModel, gaitInsNum):
        self._gaitFeaturesSetFilePath = FeaturesSetFilePath

        gaitInstanceNum = gaitInsNum
        if gaitModel == 'nm':
            seqPerGaitNum = 6
        elif gaitModel in ['bg', 'cl']:
            seqPerGaitNum = 2

        for gaitInstanceIndex in range(1, gaitInstanceNum + 1):

            # ID 34, 46, 67, 68 do not contain enough gait sequence
            if gaitModel == 'nm' and gaitInstanceIndex in [34, 46, 67, 68]:
                continue

            for seqPerGaitIndex in range(1, seqPerGaitNum + 1):

                fileNameID ='%03i' %gaitInstanceIndex
                fileNameWearID = '%02i' %seqPerGaitIndex
                fileName = fileNameID + '_' + gaitModel + '_' + \
                           fileNameWearID + '_090.csv'

                filePath = self._gaitFeaturesSetFilePath + '/' + fileName

                if not os.path.isfile(filePath):
                    print filePath, 'is Wrong !'
                else:
                    print filePath

                widthVector = []
                widthVectorLeft = []
                widthVectorRight = []

                with open(filePath, 'rb') as gaitFeatureFile:
                    gaitReader = csv.reader(gaitFeatureFile)
                    for line in gaitReader:
                        widthVector.append([int(i) for i in line[0:240]])
                        widthVectorLeft.append([int(i) for i in line[240:480]])
                        widthVectorRight.append([int(i) for i in line[480:720]])

                self.gaitWidthVectors.append(widthVector)
                self.gaitWidthVectorsLeft.append(widthVectorLeft)
                self.gaitWidthVectorsRight.append(widthVectorRight)

    def getGaitStepSeqs(self):
        for widthVector in self.gaitWidthVectors:
            self.gaitStepSeqs.append(self.getGaitStepSeq(widthVector))

    def saveGaitStepSeq(self, filePath):

        with open(filePath, 'wb') as gaitSeqFile:
            gaitSeqWriter = csv.writer(gaitSeqFile)


            for gaitSeq in self.gaitStepSeqs:
                gaitSeqWriter.writerow(gaitSeq)

        return filePath

    def getGaitStepSeq(self, gaitWidthVectors):

        steps = []

        for widthVector in gaitWidthVectors:
            heightStart, heightEnd = \
                self.findFirstAndLastNonZeroValueIndex(widthVector)
            height = heightEnd - heightStart

            steps.append(int(np.amax(
                         widthVector[heightEnd - int(height/4):heightEnd])))

        return steps

    def loadGaitStepSeq(self, filePath):

        with open(filePath, 'rb') as gaitStepFile:
            gaitSteSeqReader = csv.reader(gaitStepFile)

            for gaitStepSeq in gaitSteSeqReader:
                self.gaitStepSeqs.append(gaitStepSeq)


    def gaitFeaturesSetVerification(self):
        """

        :return:
        """

    def extractGaitHeight(self, verticalSum):
        """
            the height of a gait.
        :return:
        """
        # the difference of last pint and first nonzero point in vertical is
        # the height
        heightStart, heightEnd = \
            self.findFirstAndLastNonZeroValueIndex(verticalSum)
        return heightEnd, heightStart

    def findFirstAndLastNonZeroValueIndex(self, inputList):
        """
            for a inputList, find the first and last nonzero point
        :param inputArray:
        :return:
        """
        inputArray = np.array(inputList)

        inputLen = len(inputArray)

        # if inputList is empty raise
        if inputLen == 0:
            raise ValueError(' the input list is empty ')

        startIndex = 0  # the start pixel index of nonzero point
        endIndex = 0  # the end pixel index of nonzero point

        inputListCopy = inputArray.copy()  # a copy of input list

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

    def plotWidthVectors(self, gaitID, wearID):

        plt.figure()

        seqID = (gaitID - 1) * 6 + wearID - 1

        widthVectorLen = len(self.gaitWidthVectors[seqID])

        for widthVectorIndex in range(0, widthVectorLen):
            plt.plot(self.gaitWidthVectors[seqID][widthVectorIndex])

        plt.show()

    def saveFeaturesSet(self, gaitDataSet, FeateuresSetPath):

        if not os.path.exists(FeateuresSetPath):
            print 'Features set path is Wrong !'
            return
        else:
            print FeateuresSetPath, 'is OK !'
            self._FeaturesSetPath = FeateuresSetPath

        if not gaitDataSet or gaitDataSet._numGaitSeq < 1:
            print 'There is something wrong with gaitDataSet'
        else:
            print 'gaitDataSet is OK !'

    """
        The test result of this function:
        ID 33 only contains one gait sequence in nm-90
        ID 45,67 only contain five gait sequences in nm-90
        ID 66 only contains three gait sequences in nm-90
    """
    def featureSetFileNumTest(self, featureSetFilePath):

        fileList = os.listdir(featureSetFilePath)

        print 124*6

        print len(fileList)

        featureFileCounter = [0]*124

        for featureFile in fileList:
            featureFileInList = featureFile.split('_')
            print featureFile, int(featureFileInList[0])

            featureFileCounter[int(featureFileInList[0])-1] += 1

        #print featureFileCounter

        counter = 0
        for featureCounter in featureFileCounter:
            if featureCounter < 6:
                print 'ID', counter, ' only has ', featureCounter, \
                    ' featuresFiles'

            counter += 1

