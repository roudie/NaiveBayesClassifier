import DataConverter
import CrossValidation as cross
import MyMath
import ConfusionMatrix
import NormalDist


class GaussianManager:
    k = 1
    reapeats = 1
    raw_data = []

    def preper(self, raw_data, reapeats, k):
        d = DataConverter.list_to_dictionary(raw_data)
        self.k = k
        self.reapeats = reapeats
        self.raw_data = raw_data

    def start(self):

        measurment = []
        for i in range(self.reapeats):
            measure = []
            splitted_dataset = cross.split_list(self.raw_data, self.k, True)
            k_fold = cross.KFold(splitted_dataset)
            for fold in k_fold:
                stats = MyMath.calcNormalStats(fold[0])
                confusion_matrices = ConfusionMatrix.ConfusionMatrixStatistic(stats)
                for item in fold[1]:
                    confusion_matrices.add_result(item[len(item)-1], NormalDist.get_class(stats, item))
                measure.append(confusion_matrices.calc_stats())
            measurment.append(ConfusionMatrix.Measure.connect(measure))
        return ConfusionMatrix.Measure.connect(measurment)
