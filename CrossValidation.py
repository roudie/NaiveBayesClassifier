from sklearn.model_selection import KFold
import numpy as np
def splitDictionary(dictionary, p):
    newDict = []
    for i in range(p):
        newDict.append(dict())
    for key, value in dictionary.items():
        print(len(value))
    X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])  # create an array
    y = np.array([1, 2, 3, 4])  # Create another array
    for key, value in dictionary.items():

    #kf = KFold(n_splits=2)
    #c = kf.get_n_splits(X)

    #print(kf)
    #print("w")