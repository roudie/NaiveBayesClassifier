from NB.NaiveBayes import GaussianNB, CategoricalNB, EqualWidthPartitioning, EqualDepthPartitioning, KMeansPartitioning
import Import as imp
import numpy as np
from Validation.ConfusionMatrix import ConfusionMatrixStatistic, Measure
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Validation.CrossValidation import KFold, split_list

data = ['wine'] #, 'wine', 'glass', 'pima']
dataset_name = data[0]
iris_col = ['sepal lenght', 'sepal width', 'petal length', 'petal width', 'class']
glass_col = ["RI: refractive index", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe", "class"]
wine_col = ["Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
            "Color intensity", "Hue", "OD280/OD315", "Proline", "class"]
raw_data = imp.loadCSV("data/" + dataset_name + ".data")


sns.pairplot(pd.DataFrame(raw_data, columns=wine_col), hue="class")
plt.gcf().subplots_adjust(bottom=0.05, left=0.05)
#plt.tight_layout()
plt.show()