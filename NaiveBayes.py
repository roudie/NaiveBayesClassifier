import Import as imp
import CrossValidation as cross
import MyMath
import NormalDist
import ConfusionMatrix
import pprint
import Discretization.EqualWidthPartitioning as disc
import TestManagers.Gaussian as gau
raw_data = imp.loadCSV("data\\iris.data")
zipped = list(zip(*raw_data))

bin = 10
reapets = 10
k_fold = [2, 3, 5, 10]
gaussian = gau.GaussianManager()
stats = []
for k in k_fold:
    gaussian.preper(raw_data, reapets, k)
    stats.append(gaussian.start())

for x in stats:
    print(x)


## bining equal width
equal_wid = []
pprint.pprint(raw_data)
for i in range(len(zipped)-1):
    equal_wid.append(disc.EqualWidthPartitioning(zipped[i], 10))
for i in range(len(raw_data)):
    for j in range(len(raw_data[i])-1):
        raw_data[i][j] = equal_wid[j].bining(raw_data[i][j])




splitted_dataset = cross.split_list(raw_data, 2, True)
k_fold = cross.KFold(splitted_dataset)
measure = []
for fold in k_fold:
    stats = MyMath.calcNormalStats(fold[0])

    stat = ConfusionMatrix.ConfusionMatrixStatistic(stats)
    iter = 0
    for item in fold[1]:
        stat.add_result(item[len(item)-1], NormalDist.get_class(stats, item))
        if NormalDist.get_class(stats, item) == item[len(item)-1]:
            iter +=1
    measure.append(stat.calc_stats())

x = ConfusionMatrix.Measure.connect(measure)
#print(x)