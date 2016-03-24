'''
@file    : GaitFeaturesSet.py
@time    : Mar 15,2016 16:35
@author  : duanxxnj@163.com
'''

import os
import csv

class GaitFeaturesSet:

    def __init__(self):
        self._FeaturesSetPath = ""
        self._gaitFeaturesSetFilePath = ""
        pass

    def loadFeaturesSet(self, FeaturesSetFilePath, gaitModel):


        self._gaitFeaturesSetFilePath = FeaturesSetFilePath

        gaitInstanceNum = 124
        if gaitModel == 'nm':
            seqPerGaitNum = 6
        elif gaitModel in ['bg', 'cl']:
            seqPerGaitNum = 2

        for gaitInstanceIndex in range(1, gaitInstanceNum + 1):

            if gaitModel == 'nm' and gaitInstanceIndex in [33, 45, 66, 67]:
                continue

            for seqPerGaitIndex in range(1, seqPerGaitNum + 1):

                fileNameID ='%03i' %gaitInstanceIndex
                fileNameWearID = '%02i' %seqPerGaitIndex
                fileName = fileNameID + '_' + gaitModel + '_' + \
                           fileNameWearID + '_90.csv'
                print fileName







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

