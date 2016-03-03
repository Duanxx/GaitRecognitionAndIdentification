'''
@file    : TestGaitDataSet.py
@time    : Mar 01,2016 10:03
@author  : duanxxnj@163.com
'''

from GaitDataSet import GaitDataSet

gds = GaitDataSet()

gaitDataSetFilePath = '/home/Duanxx/Documents/GraduateDesign/gait_dataset/CASIA/DatasetB/silhouettes'

gds.loadDataSet(gaitDataSetFilePath)

gds.findAllFiles()