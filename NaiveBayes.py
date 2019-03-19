import Import as imp
import CrossValidation as cross
import MyMath
import NormalDist
import ConfusionMatrix
import pprint
import Discretization.EqualWidthPartitioning as disc
raw_data = imp.loadCSV("data\\iris.data")
zipped = list(zip(*raw_data))

equal_wid = disc.EqualWidthPartitioning(zipped[1], 5)
equal_wid.bining(2.2)
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
print(x)