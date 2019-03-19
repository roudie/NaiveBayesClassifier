def list_to_dictionary(dataset):
    d = dict()
    for i in range(len(dataset)):
        d.setdefault(
            dataset[i][len(dataset[i]) - 1], []).append(
            [float(i) for i in dataset[i][0:len(dataset[i]) - 1]])
    return d


def dictionary_to_list(dictionary):
    list = []
    for key, value in dictionary.items():
        for item in value:
            list.append([*item, key])
    return list
