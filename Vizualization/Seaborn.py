import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import Import as imp

polish = ["typ", "k_fold", 'Ilość kubełków', "Dokładność", "Precyzja", "Czułość/Swoistość", "F1"]
english = ['type', 'k_folg', 'bins', 'accuracy', 'precision', 'recall', 'F1']
current = english

def table_to_dataframe(data, dataset_name):
    #plt, ax = plt.subplots()
    datas = pd.DataFrame(data, columns=current)


    print(datas)
    sns.set(style="ticks")
    #data2 = datas['typ'].isin('Brak dyskretyzacji')

    g = sns.PairGrid(datas, hue=current[0])
    g.map_upper(plt.scatter)
    g.map_lower(sns.kdeplot)
    g.map_diag(plt.hist, histtype="step", linewidth=2);
    g.add_legend()
    g.fig.suptitle(dataset_name, size=15)

    ##sns.pairplot(datas, hue='typ')
    #sns.pairplot(y, hue="E")
    datasR = datas.round({'k_fold': 0, 'accuracy': 2, 'precision': 2, 'recall': 2, 'F1': 2, 'bins': 0})
    x = datasR.to_latex(index=False)
    f = open(dataset_name + ".txt", "w")
    f.write(x)
    f.close()

    print(datas.values)



    plt.show()
