import Import as imp
import TestManagers.Gaussian as gau
import TestManagers.BinningEqualWidth as bew

raw_data = imp.loadCSV("data\\wine.data")
zipped = list(zip(*raw_data))

bin = 10
reapets = 1
k_fold = [2, 3, 5, 10]
gaussian = gau.GaussianManager()
stats = []
for k in k_fold:
    gaussian.prepare(raw_data, reapets, k)
    stats.append(gaussian.start())



equal_width_manager = bew.EqualWidthManager()
equal_width_manager.prepare(raw_data, 10, 9)
x = equal_width_manager.start()
print(x)



#for i in range(len(zipped)-1):
#    equal_wid.append(disc.EqualWidthPartitioning(zipped[i], 10))
#for i in range(len(raw_data)):
#    for j in range(len(raw_data[i])-1):
#        raw_data[i][j] = equal_wid[j].bining(raw_data[i][j])

