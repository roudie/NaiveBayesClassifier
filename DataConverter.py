def list_to_dictionary(dataset):
    d = dict()
    for i in range(len(dataset)):
        d.setdefault(
            dataset[i][len(dataset[i]) - 1], []).append(
            [float(i) for i in dataset[i][0:len(dataset[i]) - 1]])
    return d

def list_to_bin_dictionary(dataset, p):
    d = list_to_dictionary(dataset)
    bin_dict = dict()
    for key, val in d.items():
        bin_dict[key] = [int(0) for i in range(p)]
    print(bin_dict)


def dictionary_to_list(dictionary):
    list = []
    for key, value in dictionary.items():
        for item in value:
            list.append([*item, key])
    return list
