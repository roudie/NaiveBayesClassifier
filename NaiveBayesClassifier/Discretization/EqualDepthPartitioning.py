
def get_class(stats, class_prob, buckets, item):
    prob = dict()
    result = []
    for i in range(len(item)-1):
        item[i] = buckets[i].binning(item[i])
    for key, atr in stats.items():
        for i in range(len(item) - 1):
            prob.setdefault(key, []).append(stats[key][i][item[i]])
        buff = 1
        for x in prob[key]:
            buff *= x
        result.append([key, buff * class_prob[key]])
    max = result[0]
    for x in result:
        if x[1] > max[1]:
            max = x
    return max[0]


def create_dictionary_with_buckets(raw_data, l_data, k):
    d = dict()
    buckets = []
    zipped_raw_data = list(zip(*raw_data))
    for i in range(len(zipped_raw_data) - 1):
        buckets.append(EqualDepthPartitioning(zipped_raw_data[i], k))


    ### tworzenie wygładzonego slownika

    zipped_l_data = list(zip(*l_data))
    dictonary = dict()
    class_prob = dict()
    for class_name in zipped_l_data[len(zipped_l_data) - 1]:
        if class_name not in dictonary:
            class_prob[class_name] = k
            dictonary[class_name] = []
            for j in range(len(buckets)):
                dictonary[class_name].append([int(1) for i in range(k)])


    ## uzupełnianie kubełków i liczenie prawdopodobienstwa klasy
    for item in l_data:
        for i in range(len(item) - 1):
            dictonary[item[len(item)-1]][i][buckets[i].binning(item[i])] += 1
        class_prob[item[len(item) - 1]] += 1

    ## liczenie prawdopodobieństw kubełków
    for key, val in dictonary.items():
        for atr in val:
            for i in range(len(atr)):
                atr[i]/=class_prob[key]
    for key, val in class_prob.items():
        class_prob[key]/=len(raw_data)
    return dictonary, class_prob, buckets


class EqualDepthPartitioning:
    bins = []
    def __init__(self, list, n):
        list_buff = sorted(list)
        self.bins = []
        for i in range(n-1):
            widght = round(len(list_buff)/(n-i))
            if widght<len(list_buff)-1:
                self.bins.append((list_buff[widght]+list_buff[widght+1])/2)
            #print(list)
                list_buff = list_buff[widght:]

    def binning(self, val):
        for i in range(len(self.bins)):
            if val < self.bins[i]:
                return i
        return len(self.bins)

