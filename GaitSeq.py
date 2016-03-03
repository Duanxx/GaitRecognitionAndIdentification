'''
@file    : GaitSeq.py
@time    : Feb 26,2016 10:14
@author  : duanxxnj@163.com
'''

import os
import cv2

class GaitSeq:
    """

    """
    gaitSeq = []
    stepSeq = []
    smoothedStepSeq = []
    standAndStraddle = []

    gaitSeqID = ''
    gaitSeqWear = ''
    gaitSeqWearID = ''
    gaitSeqAngle = ''

    _gaitSeqFilePath = ''

    def __init__(self, gaitSeqFilePath):
        """

        :return:
        """
        self._gaitSeqFilePath = gaitSeqFilePath


    def getGaitFilePath(self):
        """
            get the file path of gait sequence
        :return: gaitFilePath []
        """

