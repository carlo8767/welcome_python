import os.path
from itertools import combinations

import os
from collections import Counter


def combination():
    path_file = os.path.join("./file", "LZSCC.252_25-26_CW_Q2c_ciphertext.txt")

    with open(path_file) as f:
        values = f.read()
    print(values)

    length = 3
    list_pattern = [values[i:i + length] for i in range(len(values) - length + 1)]
    counter = Counter(list_pattern)
    values_length_path = [(item, count) for item, count in counter.items() if count > 1]

    occurrence = sorted(values_length_path, key=lambda item: item[1], reverse=True)
    print(occurrence)
    replace = values.replace("AUZ", "the").replace("A", "t").replace("U", "h").replace("Z", "e").replace("M","r")

    length = 5
    list_pattern = [replace[i:i + length] for i in range(len(replace) - length + 1)]
    counter = Counter(list_pattern)
    values_length_path = [(item, count) for item, count in counter.items() if count > 1]
    occurrence = sorted(values_length_path, key=lambda item: item[1], reverse=True)
    print(occurrence)
    print(replace)

    # TRY TO CHANGE THE MATCH LETTER WHT THE


combination()






#-------CALCULATION INDEX OF COINCIDENCE-------#
def split_values(values, max_splits):
    max_split = len(values) / max_splits
    separator = 0
    letters = ""
    count_key = 0
    values_split = dict()
    for ns in range(0,len(values)):
        separator+=1
        letters+=values[ns]
        values_split[count_key] = letters
        if separator > max_split:
            separator =0
            count_key+=1
            letters = ""
    return  values_split

def index_coincidence():
    path_file = os.path.join("./file", "LZSCC.252_25-26_CW_Q2c_ciphertext.txt")
    values = ""
    with (open(path_file) as f):
        values += f.read()
    dictionary_coincidence = dict()
    for n in range(1,2):
        split_dictionary = split_values(values, n)
        dictionary_coincidence [n] = coincidence_grouping_dicti(split_dictionary)

def coincidence_grouping_dicti(split_dictionary):
    index_coincidence = 0
    dictionary_occurrence = dict()
    value_counted = ''
    for x, v in split_dictionary.items():
        sorted_item = sorted(v)
        length_word = len(sorted_item)
        for n in  sorted_item:
            if value_counted == n:
                continue
            else:
                value_counted = n
                count_occ = sum( 1 for p in sorted_item if p == value_counted)
                # PROBABILITY OF DRAW TWO LETTER OF THE SAME TYPE
                index_coincidence += (float(count_occ*(count_occ-1))) / float((length_word * (length_word-1)))
            # CALCULATE INDEX OF COINCIDENCE https://en.wikipedia.org/wiki/Index_of_coincidence
        print(f'The index of coincidence is {index_coincidence}')
        index_coincidence = 0
        value_counted = ''
        dictionary_occurrence[x] = (v,index_coincidence)

        "https://realpython.com/sort-python-dictionary/"
    dictionary_occurrence = dict(sorted(dictionary_occurrence.items(), key=lambda item: item[1], reverse=True))
    print(dictionary_occurrence)
    for key, values  in dictionary_occurrence.items():
        finals = (values, split_dictionary[key])
        return  finals
    return ""
