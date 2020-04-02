import math

import numpy as np
from scipy.stats import norm
from sklearn.cluster import KMeans

class KMeansPartitioning:
    kmeans = None

    def __init__(self, list, k):
        self.kmeans = KMeans(k)
        self.kmeans.fit(np.array(list).reshape(-1, 1))

    def binning(self, list):
        return self.kmeans.predict(np.array(list).reshape(-1, 1)).tolist()


class EqualWidthPartitioning:
    min = 0
    max = 0
    n = 0
    width = 0
    bins = []

    def __init__(self, list, k):
        list = sorted(list)
        self.bins = []
        self.min = list[0]
        self.max = list[len(list)-1]
        self.width = (self.max - self.min) / (k)
        for x in range(1, k):
            self.bins.append(self.min+self.width*x)


    def binning(self, values):
        new_values = []
        for x in values:
            new_values.append(self._binning(x))
        return new_values

    def _binning(self, value):
        for bucket_id in range(len(self.bins)):
            if value < self.bins[bucket_id]:
                return bucket_id

        return len(self.bins)


class EqualDepthPartitioning: #freq
    bins = []

    def __init__(self, list, n):
        list_buff = sorted(list)
        self.bins = []
        for i in range(n-1):
            widght = round(len(list_buff)/(n-i))
            if widght<len(list_buff)-1:
                self.bins.append((list_buff[widght]+list_buff[widght-1])/2)
            #print(list)
                list_buff = list_buff[widght:]

    def binning(self, values):
        new_values = []
        for x in values:
            new_values.append(self._binning(x))
        return new_values

    def _binning(self, value):
        for i in range(len(self.bins)):
            if value < self.bins[i]:
                return i
        return len(self.bins)



class NB():
    def fit(self, x_data, y_data):
        pass

    def validate(self, x_data, y_data):
        pass

    def predict(self, x):
        pass


class GaussianNB(NB):
    def fit(self, x_data, y_data):
        self.classes = np.unique(y_data)
        self.n_features = x_data.shape[-1]
        x_data_splited = {clas: x_data[y_data==clas] for clas in self.classes}
        self.std = {k: np.std(x_data_splited[k], 0) for k, v in x_data_splited.items()}
        self.mean = {k: np.average(x_data_splited[k], 0) for k, v in x_data_splited.items()}
        self.class_prob = {k: x_data_splited[k].shape[0]/x_data.shape[0] for k in self.classes}

    def predict(self, x):
        values = {clas: np.ones(1) for clas in self.classes}
        for clas in self.classes:
            for atr_idx in range(self.n_features):
                values[clas] = values[clas] * norm(self.mean[clas][atr_idx], self.std[clas][atr_idx]).pdf(x[atr_idx])
            values[clas] = values[clas]*self.class_prob[clas]
        return max(values, key=values.get)


class CategoricalNB(NB):
    buckets = None
    prob = None
    classes = None
    n_features = None
    class_prob = None

    def fit(self, x_data, y_data, k_bin=None):
        self.classes = np.unique(y_data)
        self.n_features = x_data.shape[-1]
        zipped_x_data = list(zip(*x_data))
        self.buckets = dict()
        sum = {clas:0 for clas in self.classes}
        for clas in self.classes:
            self.buckets[clas] = dict()
            for id_atr in range(self.n_features):
                self.buckets[clas][id_atr] = dict()
                if k_bin is None:
                    unique = np.unique(zipped_x_data[id_atr])
                else:
                    unique = range(k_bin)
                for bin in unique:
                    self.buckets[clas][id_atr][bin] = 1
                    sum[clas] += 1

        for id in range(len(x_data)):
            for id_atr in range(self.n_features):
                self.buckets[y_data[id]][id_atr][x_data[id][id_atr]] += 1
                sum[y_data[id]] += 1

        self.prob = dict()
        self.class_prob = dict()
        for clas in self.classes:
            self.prob[clas] = dict()
            self.class_prob[clas] = sum[clas]/len(x_data)
            for id_atr in range(self.n_features):
                self.prob[clas][id_atr] = dict()
                if k_bin is None:
                    unique = np.unique(zipped_x_data[id_atr])
                else:
                    unique = range(k_bin)
                for bin in unique:
                    self.prob[clas][id_atr][bin] = self.buckets[clas][id_atr][bin]/(sum[clas])

    def predict(self, x):
        buff = {clas:1 for clas in self.classes}
        for clas in self.classes:
            for id_atr in range(self.n_features):
                buff[clas] *= self.prob[clas][id_atr][x[id_atr]]
            buff[clas] *= self.class_prob[clas]
        return max(buff, key=buff.get)

