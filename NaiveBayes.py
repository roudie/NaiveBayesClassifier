import pprint

import Import as imp
import TestManagers.Gaussian as gau
import TestManagers.BinningEqualWidth as bew
import TestManagers.BinningEqualDepth as bed
import Vizualization.Seaborn as viz
import time
from tqdm import tqdm

data = ['iris', 'wine', 'glass', 'pima']
dataset_name = data[3]

raw_data = imp.loadCSV("data\\" + dataset_name + ".data")
zipped = list(zip(*raw_data))

bin = [int(i) for i in range(4, 15)]
repeat = 3
k_fold = [2, 3, 5, 10]
measurement = []

#metoda, k_fold, bins, ACC, PPV, TPR, F1
## gaussian
x = 0.000001

gaussian = gau.GaussianManager()
print("\ngaussian")
for k in tqdm(range(len(k_fold)), desc="k_fold"):
    gaussian.prepare(raw_data, repeat, k_fold[k])
    single_m = gaussian.start()
    x += 0.0000001
    measurement.append(["A", k_fold[k], x , single_m.ACC, single_m.PPV, single_m.TPR, single_m.F1])

print("\nEqual width")
## equal width
equal_width_manager = bew.EqualWidthManager()
for k in tqdm(range(len(k_fold)), desc="k_fold"):
    for b in tqdm(range(len(bin)), desc="bins"):
        equal_width_manager.prepare(raw_data, repeat, k_fold[k], bin[b])
        single_m = equal_width_manager.start()
        measurement.append(["B", k_fold[k], float(bin[b]), single_m.ACC, single_m.PPV, single_m.TPR, single_m.F1])


## equal depth
print("\nEqual depth")
equal_depth_manager = bed.EqualDepthManager()
for k in tqdm(range(len(k_fold)), desc="k_fold"):
    for b in tqdm(range(len(bin)), desc="bins"):
        equal_depth_manager.prepare(raw_data, repeat, k_fold[k], bin[b])
        single_m = equal_depth_manager.start()
        measurement.append(["C", k_fold[k], float(bin[b]), single_m.ACC, single_m.PPV, single_m.TPR, single_m.F1])
#x = imp.measurement_to_dict(measurement)

viz.table_to_dataframe(measurement, dataset_name)