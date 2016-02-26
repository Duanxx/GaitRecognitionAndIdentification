'''
@file    : Gait.py
@time    : Feb 26,2016 10:16
@author  : duanxxnj@163.com
'''

class Gait:
    """

    """

    widthVector = []
    widthVectorLeft = []
    widthVectorRight = []
    height = 0.0
    stepLength = 0

    _gaitImageFrame = []

    def __init__(self, gaitImageFrame):
        """

        :param gaitImageFrame:
        :return:
        """

        self._gaitImageFrame = gaitImageFrame.copy()

    def extractWidthVector(self):
        """

        :return:
        """