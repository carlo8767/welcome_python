# You can edit this file but cannot import anything.

def task0(relations):
    # input is a dictionary of relations; output is a list of message strings to be printed,
    # e.g. ["t17 is UNION of t7 and t15", "t11 is INTERSECTION of t2 and t3", "t24 is CARTPROD of t9 and t21"]

    print(f'The relation are... {relations}')
    return []

def task1(): # returns a list of sqlite statements to create tables and populate them; 
    return []



























"""
CALCULATION IF EXIST A CARTESIAN 
A * B = C 
"""

def verification_cartesian(dictionary_relation)-> bool:
    # ITERATE OVER A SET OF LIST WITH INDEX
    list_tuple = list(dictionary_relation.values())
    dictionary_store_concat = dict()
    until = len(list_tuple)
    # FROM BEGIN TO EMD
    for firstKey, v in enumerate(list_tuple[0:until]):
        for second_key,v in enumerate(list_tuple[firstKey+1:], start=firstKey+1):
         dictionary_store_concat [firstKey, second_key]  = set_cartesian_product(list_tuple[firstKey], list_tuple[second_key])
    # FROM END TO BEGIN
    for firstKey in range(until-1,-1,-1):
        for second_key in range (firstKey-1, -1, -1):
            dictionary_store_concat[firstKey, second_key] = set_cartesian_product(list_tuple[firstKey], list_tuple[second_key])
    # MISS CARLO RETURN THE MESSAGE
    return find_occurrence_cartesian(dictionary_store_concat,dictionary_relation)



# EXTRACT CARTESIAN PRODUCTION BETWEEN TUPLES
def set_cartesian_product(set_tuple_one, set_tuple_two)-> set:
    set_record = set()
    for external in set_tuple_one:
        for internal in set_tuple_two:
            concat = external + internal
            set_record.add(concat)
    return set_record

# VERIFICATION IF THERE IS A CARTESIAN
def find_occurrence_cartesian (dictionary_cartesian, original_dictionary)-> bool:
    result = False
    for k in dictionary_cartesian.keys():
        for ik in original_dictionary.keys():
            if dictionary_cartesian[k] == original_dictionary[ik]:
                result = True
                return  result
    return  result


