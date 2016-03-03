'''
@file    : GaitDataSet.py
@time    : Feb 26,2016 10:41
@author  : duanxxnj@163.com
'''

from GaitSeq import GaitSeq
import os

class GaitDataSet:
    """

    """

    _gaitDataSetPath = ''
    _numGaitSeq = 0

    data = []

    def __init__(self):
        """

        :param gaitDataSetPath:
        :return:
        """

    def loadDataSet(self, dataSetFilePath):
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

    def findAllFiles(self):
        for root, dirs, files in os.walk(self._gaitDataSetPath):

            if len(files) == 0:
                continue
            elif os.path.basename(root) == 'silhouettes':
                continue
            else:

                self.data.append(GaitSeq(root))
                print self.data[self._numGaitSeq]._gaitSeqFilePath
                self._numGaitSeq += 1
                raw_input()