import scipy.stats
import pprint
def GetClass(stats, item):
    prob = dict()
    result = []
    for key, atr in stats.items():
        #print(atr)
        for x in range(len(item)):
            prob.setdefault(key, []).append(scipy.stats.norm(stats[key][x][0], stats[key][x][1]).pdf(item[x]))
        #prob.append(scipy.stats.norm(100, 12).pdf(95))
        buff = 1
        for x in prob[key]:
            buff*=x
        result.append([key, buff])
    max = result[0]
    for x in result:
        if x[1] > max[1]:
            max = x
    return max[0]
    #pprint.pprint(result)
    #pprint.pprint(prob)
