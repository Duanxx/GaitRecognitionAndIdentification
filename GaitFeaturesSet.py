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

    def loadFeaturesSet(self, FeaturesSetFilePath):

        if not os.path.isfile(FeaturesSetFilePath):
            print 'File path is wrong !'
            return
        else:
            print FeaturesSetFilePath, ' is OK !'
            self._gaitFeaturesSetFilePath = FeaturesSetFilePath

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

    def featureSetFileNumTest(self, featureSetFilePath):

        fileList = os.listdir(featureSetFilePath)

        print 124*6

        print len(fileList)

        featureFileCounter = [0]*124

        for featureFile in fileList:
            featureFileInList = featureFile.split('_')
            print featureFile, int(featureFileInList[0])

            featureFileCounter[int(featureFileInList[0])-1] += 1

        print featureFileCounter

        counter = 0
        for featureCounter in featureFileCounter:
            if featureCounter < 6:
                print featureCounter, counter

            counter += 1

