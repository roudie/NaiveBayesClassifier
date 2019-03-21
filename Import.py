import csv

def loadCSV(filename):
    lines = csv.reader(open(filename, 'rt'))
    dataset = list(lines)
    for line in dataset:
        for x in range(len(line)-1):
            line[x] = float(line[x])
    return dataset


def splitDataset(dataset):
    d = dict()
    for i in range(len(dataset)):
        d.setdefault(
            dataset[i][len(dataset[i])-1], []).append(
            [float(i) for i in dataset[i][0:len(dataset[i])-1]])
    return d


def measurement_to_dict(dataset):
    d = dict()
    for i in range(len(dataset)):
        d.setdefault(
            dataset[i][0], []).append(
            [float(i) for i in dataset[i][1:len(dataset[i])]])
    return d