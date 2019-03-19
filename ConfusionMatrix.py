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
            self.PPV = (matrix.TP)/(matrix.TP + matrix.FP)
            self.TNR = (matrix.TN)/(matrix.FP + matrix.TN)
            self.TPR = (matrix.TP)/(matrix.TP + matrix.FN)
            self.F1  = (2*self.PPV*self.TPR)/(self.PPV + self.TPR)

    def __str__(self):
        ret_str = "F1: " + str(self.F1) + "\nACC: "+str(self.ACC) + "\nPPV: "+ str(self.PPV)
        ret_str += "\nTNR: " + str(self.TNR) + "\nTPR: " + str(self.TPR)
        return ret_str

    @staticmethod
    def connect(dict):
        measure = Measure(None)
        iter = 0
        for val in dict:
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

    def __init__(self, dict):

        for key, value in dict.items():
            self.relative_matrices[key] = ConfusionMatrix()

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


    def calc_stats(self):
        stats = dict()
        for key, value in self.relative_matrices.items():
            stats[key] = Measure(value)
        return stats
