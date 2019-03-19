from random import shuffle
import DataConverter

def split_list(dataset, p, random):
    list = []
    for i in range(p):
        list.append([])
    iter = 0
    if random:
        shuffle(dataset)
    for item in dataset:
        list[iter].append(item)
        iter = (iter + 1) % p
    return list


def KFold(list):
    return_list = []
    for i in range(len(list)):
        list_buffor = []
        for j in range(len(list)):
            if i != j:
                list_buffor = list_buffor + list[j]
        return_list.append([DataConverter.list_to_dictionary(list_buffor), list[i]])
    return return_list

def split_dictionary(dictionary, p, random):
    newDict = []
    iter = 0
    for i in range(p):
        newDict.append(dict())
    for key, value in dictionary.items():
        print(len(value))
        for item in value:
            newDict[iter].setdefault(key, []).append(item)
            iter = (iter+1) % p
    return newDict


def dictionary_to_raw(dictionary):
    list = []
    for key, value in dictionary.items():
        for item in value:
            x = item
            list.append([*item, key])
    return list


def split(dictionary, p, random):
    splitted = split_dictionary(dictionary, p, random)
    list = []
    for dict in splitted:
        n_dict = dict()



