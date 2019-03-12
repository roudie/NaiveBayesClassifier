
import pprint
import Import as imp
import MyMath as mmath
dataset = imp.loadCSV("data\\iris.data")

stats = mmath.calcNormalStats(dataset)

pprint.pprint(list(dataset.items()))
pprint.pprint(stats)
