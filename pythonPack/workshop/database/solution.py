# You can edit this file but cannot import anything.
# MESSAGE RESULT
message_cartesian = "is CARTPROD of"
message_no_match = "NO MATCH"
message_intersection = "is INTERSECTION of"
message_union = "is UNION of"



def task0(relations):
    # input is a dictionary of relations; output is a list of message strings to be printed,
    # e.g. ["t17 is UNION of t7 and t15", "t11 is INTERSECTION of t2 and t3", "t24 is CARTPROD of t9 and t21"]
    list_message = list()
    # VERIFICATION MULTIPLE RELATION IN A DB  ?
    result_intersection = verify_intersection(relations)
    result_cartesian = verification_cartesian(relations)
    result_union = verify_union(relations)

    if not result_union  and not result_cartesian and not result_intersection:
        print("ENTER HERE EMPTY")
        list_message.append(message_no_match)
    else:
        if  result_union:
            print("ENTER HERE UNION")
            append_result_cart_union_inter(list_message, result_union)
        if  result_cartesian:
            print("ENTER HERE CARTESIAN")
            append_result_cart_union_inter(list_message, result_cartesian)
        if  result_intersection:
            print("ENTER HERE INTERSECTION")
            append_result_cart_union_inter(list_message, result_intersection)
    return list_message
def task1(): # returns a list of sqlite statements to create tables and populate them; 
    return []



" APPEND RESULT "

def append_result_cart_union_inter (list_message, list_result):
    for values in list_result:
        list_message.append(values)


" CALCULATION UNION "


def verify_union (dictionary_relation):
    list_message = list()
    sets_list = list(dictionary_relation.values())
    dictionary_union = dict()
    for key_external, value in enumerate(sets_list[0:len(sets_list) - 1]):
        for key_internal, internal_value in enumerate(sets_list[(key_external + 1):], start=key_external + 1):
            union_set = value.union(internal_value).copy()
            if value.issubset(internal_value) or internal_value.issubset(value):
                continue
            dictionary_union[(key_external, key_internal)] = union_set

    for external_key in dictionary_union.keys():
        for internal_key in dictionary_relation.keys():
            if dictionary_union[external_key] == dictionary_relation[internal_key]:
                # VERIFY IF THEY WANT DUPLICATE
                message_return = f'{internal_key} {message_union} t{external_key[0]} and t{external_key[1]}'
                list_message.append(message_return)
    return list_message



" CALCULATION INTERSECTION "

# EXTRACT THE VALUE
def verify_intersection(dictionary_relation):
   list_message = list()
   # VERIFY IF THERE IS ONLY ONE MESSAGE
   sets_list = list(dictionary_relation.values())
   dictionary_interset = dict()
   for key_external, v in enumerate(sets_list[0:len(sets_list)-1]):
       external = sets_list[key_external]
       for key_internal, x in enumerate(sets_list[key_external+1:], start=1):
        if v.issubset(x) or x.issubset(v):
               continue
        result = external.intersection(x)
        if result:
            dictionary_interset[key_external, key_internal] = result
            break # CANNOT HAVE MORE THAN ONE INTERSECTION
   for unpack in dictionary_interset.keys():
       for internal_unpack in dictionary_relation.keys():
           if dictionary_interset[unpack] == dictionary_relation [internal_unpack]:
               message_result = f'{internal_unpack} {message_intersection} t{unpack[0]} and t{unpack[1]}'
               list_message.append(message_result)
   return  list_message

"""
CALCULATION IF EXIST A CARTESIAN 
A * B = C 
"""

def verification_cartesian(dictionary_relation)-> list:
    # ITERATE OVER A SET OF LIST WITH INDEX
    list_tuple = list(dictionary_relation.values())
    dictionary_store_concat = dict()
    until = len(list_tuple)
    # FROM BEGIN TO EMD
    for firstKey, extv in enumerate(list_tuple[0:until]):
        for second_key,interv in enumerate(list_tuple[firstKey+1:], start=firstKey+1):
         # CONSTRAINT SUBSET
         if extv.issubset(interv) or extv.issubset(interv):
            continue
         dictionary_store_concat [firstKey, second_key]  = set_cartesian_product(list_tuple[firstKey], list_tuple[second_key])
    # FROM END TO BEGIN
    for firstKey in range(until-1,-1,-1):
        for second_key in range (firstKey-1, -1, -1):
            if list_tuple[firstKey].issubset(list_tuple[second_key]) or list_tuple[second_key].issubset(list_tuple[firstKey]):
                continue
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
def find_occurrence_cartesian (dictionary_cartesian, original_dictionary)-> list:
    list_message = list()
    for k in dictionary_cartesian.keys():
        for ik in original_dictionary.keys():
            if dictionary_cartesian[k] == original_dictionary[ik]:
                message = f'{ik} {message_cartesian} t{k[0]} and t{k[1]} '
                list_message.append(message)
    return  list_message


