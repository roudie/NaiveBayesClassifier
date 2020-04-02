from random import shuffle
from NaiveBayesClassifier import DataConverter
import numpy as np

def split_list(dataset, p, random, stratyfication):
    if random:
        shuffle(dataset)
    list = []
    for i in range(p):
        list.append([])
    iter = 0
    if stratyfication:
        dataset.sort(key = lambda x:x[-1])
    for item in dataset:
        list[iter].append(item)
        iter = (iter + 1) % p
    return list




def KFold(dataset, k=5, random=True, stratification = True):
    list = split_list(dataset, k, random, stratification)
    return_list = []
    for i in range(len(list)):
        list_buffor = []
        for j in range(len(list)):
            if i != j:
                list_buffor = list_buffor + list[j]
        return_list.append([list_buffor, list[i]])
    return return_list

def KFold_str(list):
    pass

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
