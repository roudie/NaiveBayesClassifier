import scipy.stats
import NaiveBayesClassifier.DataConverter

def get_class(stats, class_prob, item):
    """
    :param stats: statystyki w słowniku z klasami.
                    Każde pole posiada k atrybutów zawierających mean i std
    :param item: przedmiot do klasyfikacji. Ostatni element to klasa przewidywana
    :return: klasa wyliczona na podstawie naivnego bayesa
    """
    prob = dict()
    result = []
    for key, atr in stats.items():
        for x in range(len(item)-1):
            prob.setdefault(key, []).append(scipy.stats.norm(stats[key][x][0], stats[key][x][1]).pdf(item[x]))
        buff = 1
        for x in prob[key]:
            buff*=x
        result.append([key, buff*class_prob[key]])
    max = result[0]
    for x in result:
        if x[1] > max[1]:
            max = x
    return max[0]


def get_mean_std(list):
    """
    :param list:
    :return: turple z wyliczoną średnią i odchyleniem standardowym
    """
    sum = 0
    amount = 0
    for x in list:
        sum+=x
        amount+=1
    average = sum/amount
    '''std = sqrt( 1/(n-1)* suma kwadratów odleglosci od sred'''
    std = 0
    for x in list:
        std+= pow(average-x, 2)
    std /= (amount-1)
    std = std**(1/2)
    return average, std


def calc_normal_stats(dataset):
    """
    :param dataset: słownik z rodziałem na klasy
    :return: słownik z podziałem na klasy z wyliczonymi mean i std dla każdego atrybutu
                oraz slownik z prawdopodonienstwem klas
    """
    stats = dict()
    dataset = NaiveBayesClassifier.DataConverter.list_to_dictionary(dataset)
    for key, value in dataset.items():
        zipped = list(zip(*value))
        for atr in zipped:
            stats.setdefault(key, []).append(get_mean_std(atr))
    return stats, get_class_prob(dataset)


def get_class_prob(dictionary):
    d = dict()
    amount = 0
    for val in dictionary.values():
        amount += len(val)
    for key, val in dictionary.items():
        d[key] = len(val)/amount
    return d

