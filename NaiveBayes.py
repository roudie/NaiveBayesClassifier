import pprint

import Import as imp
import TestManagers.Gaussian as gau
import TestManagers.BinningEqualWidth as bew
import TestManagers.BinningEqualDepth as bed
import Vizualization.Seaborn as viz
raw_data = imp.loadCSV("data\\iris.data")
zipped = list(zip(*raw_data))

bin = [8, 9, 10, 11, 12, 13, 14, 15, 16]
repeat = 2
k_fold = [2, 3, 5, 10]
measurement = []

#metoda, k_fold, bins, ACC, PPV, TPR, F1
## gaussian
x = 0.000001
gaussian = gau.GaussianManager()
for k in k_fold:
    gaussian.prepare(raw_data, repeat, k)
    single_m = gaussian.start()
    x += 0.0000001
    measurement.append(["Brak dyskretyzacji", k, x , single_m.ACC, single_m.PPV, single_m.TPR, single_m.F1])

## equal width
equal_width_manager = bew.EqualWidthManager()
for k in k_fold:
    for b in bin:
        equal_width_manager.prepare(raw_data, repeat, k, b)
        single_m = equal_width_manager.start()
        measurement.append(["Dyskretyzacja o stałej szerokości", k, float(b), single_m.ACC, single_m.PPV, single_m.TPR, single_m.F1])


## equal depth
equal_depth_manager = bed.EqualDepthManager()
for k in k_fold:
    for b in bin:
        equal_depth_manager.prepare(raw_data, repeat, k, b)
        single_m = equal_depth_manager.start()
        measurement.append(["Dyskretyzacja o stałej częstości", k, float(b), single_m.ACC, single_m.PPV, single_m.TPR, single_m.F1])
#x = imp.measurement_to_dict(measurement)
viz.table_to_dataframe(measurement)