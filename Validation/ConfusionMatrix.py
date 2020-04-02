class ConfusionMatrix:
    TP = 0
    TN = 0
    FP = 0
    FN = 0


class Measure:
    ACC = 0
    PPV = 0
    TNR = 0
    TPR = 0
    F1 = 0

    def __init__(self, matrix):
        if matrix is not None:
            self.ACC = (matrix.TP + matrix.TN)/(matrix.TP + matrix.TN + matrix.FP + matrix.FN)
            if matrix.TP + matrix.FP != 0:
                self.PPV = (matrix.TP)/(matrix.TP + matrix.FP)
            else:
                self.PPV = 1
            if matrix.FP + matrix.TN != 0:
                self.TNR = (matrix.TN)/(matrix.FP + matrix.TN)
            else:
                self.TNR = 1
            if matrix.TP + matrix.FN != 0:
                self.TPR = (matrix.TP)/(matrix.TP + matrix.FN)
            else:
                self.TPR = 1
            if self.PPV + self.TPR != 0:
                self.F1 = (2*self.PPV*self.TPR)/(self.PPV + self.TPR)
            else:
                self.F1 = 1
    def __str__(self):
        ret_str = "F1: " + str(self.F1) + "\nACC: "+str(self.ACC) + "\nPPV: "+ str(self.PPV)
        ret_str += "\nTNR: " + str(self.TNR) + "\nTPR: " + str(self.TPR)
        return ret_str

    @staticmethod
    def connect(list):
        measure = Measure(None)
        iter = 0

        for val in list:
            if type(val) is Measure:
                measure.F1 += val.F1
                measure.TPR += val.TPR
                measure.PPV += val.PPV
                measure.TNR += val.TNR
                measure.ACC += val.ACC
                iter += 1
            else:
                for key, item in val.items():
                    measure.F1  += item.F1
                    measure.TPR += item.TPR
                    measure.PPV += item.PPV
                    measure.TNR += item.TNR
                    measure.ACC += item.ACC
                    iter+=1
        measure.F1  /= iter
        measure.TPR /= iter
        measure.PPV /= iter
        measure.TNR /= iter
        measure.ACC /= iter
        return measure


class ConfusionMatrixStatistic:
    relative_matrices = dict()

    def __init__(self, dictionary: dict=None, list=None):
        if list is not None:
            for item in list:
                self.relative_matrices[item] = ConfusionMatrix()
        elif dictionary is not None:
            for key, value in dictionary.items():
                self.relative_matrices[key] = ConfusionMatrix()
        else:
            print("error init confusion matrix")

    def add_result(self, expected, received):
        for key, value in self.relative_matrices.items():
            if expected==received:
                if expected==key:
                    self.relative_matrices[key].TP+=1
                else:
                    self.relative_matrices[key].TN+=1
            else:
                if received==key:
                    self.relative_matrices[key].FP+=1
                else:
                    self.relative_matrices[key].FN+=1

    def calc_stats(self, avg = False):
        stats = dict()
        for key, value in self.relative_matrices.items():
            stats[key] = Measure(value)

        return stats


