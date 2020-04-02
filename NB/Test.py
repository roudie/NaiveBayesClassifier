from Validation import ConfusionMatrix, CrossValidation as cross
from NaiveBayesClassifier import NormalDist


class GaussianManager:
    k = 1
    repeat = 1
    raw_data = []

    def prepare(self, k_fold: int, k_fold_meth, raw_data):
        self.k = k_fold
        self.k_fold_meth = k_fold_meth
        self.raw_data = raw_data

    def start(self):
        #measurement = []


        measure = []
        splitted_dataset = cross.split_list(self.raw_data, self.k, True)
        k_fold = cross.KFold(splitted_dataset)
        for fold in k_fold:
            stats, class_prob = NormalDist.calc_normal_stats(fold[0])
            confusion_matrices = ConfusionMatrix.ConfusionMatrixStatistic(stats)
            for item in fold[1]:
                confusion_matrices.add_result(item[len(item)-1], NormalDist.get_class(stats, class_prob, item))
            measure.append(confusion_matrices.calc_stats())
        #measurement.append(ConfusionMatrix.Measure.connect(measure))

        return ConfusionMatrix.Measure.connect(measure)
