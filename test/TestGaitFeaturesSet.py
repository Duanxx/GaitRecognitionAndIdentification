'''
@file    : TestGaitFeatureSet.py
@time    : Mar 23,2016 13:07
@author  : duanxxnj@163.com
'''

from GaitFeaturesSet import GaitFeaturesSet
import matplotlib.pyplot as plt


filePath = '/home/Duanxx/Documents/GraduateDesign/gait_dataset/' \
           'CASIA/DatasetB/silhouettesFeatures/nm'

gfs = GaitFeaturesSet()

gfs.loadFeaturesSet('/home/Duanxx/Documents/GraduateDesign/gait_dataset/'
                          'CASIA/DatasetB/silhouettesFeatures/nm',
                    'nm',
                    124)

#gfs.getGaitStepSeqs()
#gfs.saveGaitStepSeq(filePath+'/nmGaitStepSeq.csv')

gfs.loadGaitStepSeq(filePath+'/nmGaitStepSeq.csv')

