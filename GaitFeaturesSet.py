'''
@file    : GaitFeaturesSet.py
@time    : Mar 15,2016 16:35
@author  : duanxxnj@163.com
'''

import os

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





    def findAllFeatures(self, loadNum = 10):
        pass