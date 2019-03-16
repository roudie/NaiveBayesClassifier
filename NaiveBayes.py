
import pprint
import Import as imp
import numpy as np
import MyMath as mmath
import NormalDist as norm
import matplotlib.pyplot as plt
import CrossValidation as cross

raw_data = imp.loadCSV("data\\iris.data")
splitted_data = imp.splitDataset(raw_data)
stats = mmath.calcNormalStats(splitted_data)

cross.splitDictionary(splitted_data, 3)
#positive_result = 0
#for key, datas in splitted_data.items():
#    for item in datas:
#        if key == norm.GetClass(stats, item):
#            positive_result+=1
        #else:
            #print(["prawidłowo: ", key, "wyszlo: ", norm.GetClass(stats, item), item])

#print(positive_result / len(raw_data))