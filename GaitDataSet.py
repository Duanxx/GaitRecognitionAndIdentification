'''
@file    : GaitDataSet.py
@time    : Feb 26,2016 10:41
@author  : duanxxnj@163.com
'''

from GaitSeq import GaitSeq
import os

class GaitDataSet:

    def __init__(self):
        self._gaitDataSetPath = ""
        self._numGaitSeq = 0

        self.data = []

    def loadDataSet(self, dataSetFilePath,  showImage=False, loadNum=10):
        """

        :param dataSetFilePath:
        :return:
        """

        if not os.path.exists(dataSetFilePath):
            print 'path is wrong!'
            return
        else:
            print 'path is OK!'
            self._gaitDataSetPath = dataSetFilePath
            print dataSetFilePath

        self.findAllFiles(showImage=showImage,loadNum=loadNum)

    def findAllFiles(self, showImage=False, loadNum=10):
        for root, dirs, files in os.walk(self._gaitDataSetPath):

            rootInList = root.split('/')

            if len(files) == 0:
                continue
            elif os.path.basename(root) == 'silhouettes':
                continue
            elif rootInList[-1] == '090' and \
                    rootInList[-2] in ['nm-01', 'nm-02']:

                self.data.append(GaitSeq(root, showImage))
                print root, '\t', len(self.data[-1].gaitSeq)
                self._numGaitSeq += 1

                if self._numGaitSeq == loadNum:
                    break
