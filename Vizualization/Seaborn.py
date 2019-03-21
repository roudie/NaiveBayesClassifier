import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import Import as imp

def table_to_dataframe(data):
    #plt, ax = plt.subplots()
    x = imp.loadCSV("data\\iris.data")
    datas = pd.DataFrame(data, columns=["typ", "k_fold", "poziom dyskretyzacji", "ACC", "PPV", "TPR", "F1"])
    datas.to_csv("s.csv")
    print(x)
    print(datas)
    sns.set(style="ticks")
    sns.pairplot(datas, hue="typ")
    print(datas.values)
    plt.show()

#x = imp.loadCSV("..\\data\\iris.data")
#y = pd.DataFrame(x, columns=["A","B","C","D","E"])
#sns.set(style="ticks")
#sns.pairplot(y, hue="E")
#plt.show()