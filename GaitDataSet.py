'''
@file    : GaitDataSet.py
@time    : Feb 26,2016 10:41
@author  : duanxxnj@163.com
'''

from GaitSeq import GaitSeq
import os
import csv


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

        self.findAllFiles(showImage=showImage, loadNum=loadNum)

    def findAllFiles(self, showImage=False, loadNum=10):
        for root, dirs, files in os.walk(self._gaitDataSetPath):

            rootInList = root.split('/')

            if len(files) == 0:
                continue
            elif os.path.basename(root) == 'silhouettes':
                continue
            elif rootInList[-1] == '090' and \
                    rootInList[-2] in ['nm-01', 'nm-02']:

                gaitSeq = GaitSeq(root, showImage)

                #self.data.append(gaitSeq)
                self.saveGaitSeqAsCSV(gaitSeq)

                #print root, '\t', len(self.data[-1].gaitSeq)
                self._numGaitSeq += 1

                if self._numGaitSeq == loadNum:
                    break

    def saveGaitSeqAsCSV(self, gaitSeq):
        """

        :param gaitSeq:
        :return:
        """

        fileName = gaitSeq.gaitSeqID + "_" +\
                   gaitSeq.gaitSeqWear + "_"+\
                   gaitSeq.gaitSeqWearID + "_"+\
                   gaitSeq.gaitSeqAngle + ".csv"

        #filePath = gaitSeq._gaitSeqFilePath + "/" + fileName

        filePath = "/home/Duanxx/Documents/GraduateDesign/gait_dataset/CASIA" \
            "/DatasetB/silhouettesFeatures/" + fileName

        print filePath

        with open(filePath, 'wb') as gaitSeqFile:
            gaitSeqWriter = csv.writer(gaitSeqFile)

            # gaitSeqAttriList is splitted with '*'
            gaitSeqAttriList = gaitSeq.standGaits + ['*'] +\
                               gaitSeq.straddleGaits + ['*'] +\
                               gaitSeq.stepSeq

            gaitSeqWriter.writerow(gaitSeqAttriList)

            for gait in gaitSeq.gaitSeq:
                gaitSeqWriter.writerow(gait.widthVector +
                                       gait.widthVectorLeft +
                                       gait.widthVectorRight)
