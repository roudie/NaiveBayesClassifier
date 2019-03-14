import csv

def loadCSV(filename):
    lines = csv.reader(open(filename, 'rt'))
    dataset = list(lines)
    return dataset

def splitDataset(dataset):
    d = dict()
    for i in range(len(dataset)):
        d.setdefault(
            dataset[i][len(dataset[i])-1], []).append(
            [float(i) for i in dataset[i][0:len(dataset[i])-1]])
    return d

#[float(i) for i in lst]
