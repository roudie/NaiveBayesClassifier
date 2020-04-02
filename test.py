from NB.NaiveBayes import GaussianNB, CategoricalNB, EqualWidthPartitioning, EqualDepthPartitioning, KMeansPartitioning
import Import as imp
import numpy as np
from Validation.ConfusionMatrix import ConfusionMatrixStatistic, Measure
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Validation.CrossValidation import KFold, split_list

data = ['seeds'] #, 'wine', 'glass', 'pima']
dataset_name = data[0]


raw_data = imp.loadCSV("data/" + dataset_name + ".data")


#sns.pairplot(pd.DataFrame(raw_data, columns=['sepal lenght', 'sepal width', 'petal length', 'petal width', 'class']), hue="class")
#plt.show()
from sklearn.cluster import KMeans

#classifiers = [GaussianNB, CategoricalNB]
dicretizations = [KMeansPartitioning, EqualWidthPartitioning, EqualDepthPartitioning]

measurment = []
## GaussianNB
classifier = GaussianNB
k_folds = [2, 5, 10]


for k_fold in k_folds:
    for strat in [True, False]:
        c = KFold(raw_data, k_fold, True, strat)
        m = []
        for folds in c:
            test_zipped = list(zip(*folds[1]))
            train_zipped = list(zip(*folds[0]))

            x_train = np.array(list(zip(*train_zipped[:-1])))
            y_train = np.array(train_zipped[-1])

            x_test = np.array(list(zip(*test_zipped[:-1])))
            y_test = np.array(test_zipped[-1])

            model = classifier()
            model.fit(x_data=x_train, y_data=y_train)

            conf_matrix = ConfusionMatrixStatistic(list=list(np.unique(y_train)))
            for i in range(len(x_test)):
                conf_matrix.add_result(y_test[i], model.predict(x_test[i]))
            m.append(conf_matrix.calc_stats())
        buff = Measure.connect(m)
        measurment.append(["Gaussian", k_fold, strat, 0, buff.ACC, buff.PPV, buff.TPR, buff.F1])
        #measurment.append(Measure.connect(m))
#####





## Categorical
classifier = CategoricalNB
dicretizations = [KMeansPartitioning, EqualWidthPartitioning, EqualDepthPartitioning]
k_bins = [5, 7, 10]
k_folds = [2, 5, 10]

for discr in dicretizations:
    for k_bin in k_bins:
        ## dyskretyzacja:
        zipped = list(zip(*raw_data))
        for atr_ids in range(len(zipped) - 1):
            partitioning = discr(zipped[atr_ids], k_bin)
            zipped[atr_ids] = partitioning.binning(zipped[atr_ids])
        raw_data = list(zip(*zipped))

        for k_fold in k_folds:
            for strat in [True, False]:
                c = KFold(raw_data, k_fold, True, strat)
                m = []
                for folds in c:
                    test_zipped = list(zip(*folds[1]))
                    train_zipped = list(zip(*folds[0]))

                    x_train = np.array(list(zip(*train_zipped[:-1])))
                    y_train = np.array(train_zipped[-1])

                    x_test = np.array(list(zip(*test_zipped[:-1])))
                    y_test = np.array(test_zipped[-1])

                    model = classifier()
                    model.fit(x_data=x_train, y_data=y_train, k_bin=k_bin)

                    conf_matrix = ConfusionMatrixStatistic(list=list(np.unique(y_train)))
                    for i in range(len(x_test)):
                        conf_matrix.add_result(y_test[i], model.predict(x_test[i]))
                    m.append(conf_matrix.calc_stats())
                buff = Measure.connect(m)
                measurment.append([discr.__name__, k_fold, strat, k_bin, buff.ACC, buff.PPV, buff.TPR, buff.F1])
                #measurment.append(Measure.connect(m))
##
datas = pd.DataFrame(measurment, columns=["Model", "k_fold", "Stratyfikacja", "Bins", "Acc", "Prec", "Rec", "Fsc"])
datas.to_csv(dataset_name+".csv", index=False)
#sns.PairGrid(datas[["Model", "k_fold", "Stratyfikacja", "Bins", "Acc"]])
#plt.show()
