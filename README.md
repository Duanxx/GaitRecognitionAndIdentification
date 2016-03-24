# GaitRecognitionAndIdentification
Gait Recognition And Identification

First init a GaitDataSet object gds = GaitDataSet()

and use gds.loadDataSet(DataSetFilePath) to load the gait data set

the data set file path is the absolute path of silhouettes


TO CONFIG:

gaitDataSetFilePath in GaitIdentifaicationWithDTW.py
FeaturesFilePath in GaitDataSet.py->saveGaitSeqAsCSV()
FeaturesSelection in GaitDataSet.py-.findAllFiles()
