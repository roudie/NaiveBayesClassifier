import pprint
from NaiveBayesClassifier import DataConverter
import NaiveBayesClassifier.Discretization.EqualWidthPartitioning as ewp
from Validation import ConfusionMatrix, CrossValidation as cross

class EqualWidthManager:
    k = 1
    repeat = 1
    raw_data = []

    def prepare(self, raw_data, repeat, k):
        self.k = k
        self.repeat = repeat
        self.raw_data = raw_data

    def start(self):
        measurement = []
        for i in range(self.repeat):
            measure = []
            splitted_dataset = cross.split_list(self.raw_data, self.k, True)
            k_fold = cross.KFold(splitted_dataset)
            for fold in k_fold:
                stats, class_prob, buckets = ewp.create_dictionary_with_buckets(self.raw_data, self.k)
                confusion_matrices = ConfusionMatrix.ConfusionMatrixStatistic(stats)
                for item in fold[1]:
                    confusion_matrices.add_result(item[len(item) - 1], ewp.get_class(stats, class_prob, buckets, item))
                measure.append(confusion_matrices.calc_stats())
            measurement.append(ConfusionMatrix.Measure.connect(measure))
        return ConfusionMatrix.Measure.connect(measurement)


