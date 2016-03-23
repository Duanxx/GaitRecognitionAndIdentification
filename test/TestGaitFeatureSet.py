'''
@file    : TestGaitFeatureSet.py
@time    : Mar 23,2016 13:07
@author  : duanxxnj@163.com
'''

from GaitFeaturesSet import GaitFeaturesSet


gfs = GaitFeaturesSet()

gfs.featureSetFileNumTest("/home/Duanxx/Documents/GraduateDesign/gait_dataset"+
                          "/CASIA/DatasetB/silhouettesFeatures")