import pprint


def getNormal(list):
    sum = 0
    amount = 0
    for x in list:
        sum+=x
        amount+=1
    average = sum/amount
    ##  std = sqrt( 1/(n-1)* suma kwadratów odleglosci od sred
    std = 0
    for x in list:
        std+= pow(average-x, 2)
    std /= (amount-1)
    std = std**(1/2)
    return average, std


def calcNormalStats(dataset):
    stats = dict()
    for key, value in dataset.items():
        zipped = list(zip(*value))
        for atr in zipped:
            #print(atr)
            stats.setdefault(key, []).append(getNormal(atr))
    #z = stats.update(stats)
    #pprint.pprint(Merge(stats, stats))
    return stats


def Merge(dict1, dict2):
    return(dict2.update(dict1))
