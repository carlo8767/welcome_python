# You can edit this file but cannot import anything.
# MESSAGE RESULT

INDEX_CREATE_TABLE = list()
DICTIONARY_TABLE = dict()
message_cartesian = "is CARTPROD of"
message_no_match = "NO MATCH"
message_intersection = "is INTERSECTION of"
message_union = "is UNION of"
list_insert_db = list()

def task0(relations):
    # input is a dictionary of relations; output is a list of message strings to be printed,
    # e.g. ["t17 is UNION of t7 and t15", "t11 is INTERSECTION of t2 and t3", "t24 is CARTPROD of t9 and t21"]
    list_message = list()
    # VERIFICATION MULTIPLE RELATION IN A DB  ?
    result_intersection = verify_intersection(relations)
    result_cartesian = verification_cartesian(relations)
    result_union = verify_union(relations)

    if not result_union  and not result_cartesian and not result_intersection:
        list_message.append(message_no_match)
    else:
        if  result_union:
            append_result_cart_union_inter(list_message, result_union)
        if  result_cartesian:
            append_result_cart_union_inter(list_message, result_cartesian)
        if  result_intersection:
            append_result_cart_union_inter(list_message, result_intersection)
    return list_message


def task1(): # returns a list of sqlite statements to create tables and populate them;
    list_message = list()
    list_create = create_statement()
    list_insert = insert_statement()
    if list_create:
        append_query(list_message, list_create)
    if list_insert:
        append_query(list_message, list_insert)
    return list_message


""" TASK 1 CREATION QUERY CREATE AND INSERT """
def append_query (list_message, list_result):
    for values in list_result:
        list_message.append(values)

def create_statement():
    list_statement = list()
    for extract_key in INDEX_CREATE_TABLE:
        # EXTRACT THE SIZE OF THE TUPLE
        size_insert_value = DICTIONARY_TABLE[extract_key]
        for p in size_insert_value:
            prepare_statement = f'CREATE TABLE'
            size = len(p)
            prepare_statement += f' {extract_key} ('
            for n in range(0, size):
                if size - 1 == n:
                    prepare_statement += f' c{n} INTEGER ) ;'
                else:
                    prepare_statement += f' c{n} INTEGER, '
            list_statement.append(prepare_statement)
            break
    return list_statement

def insert_statement():
        list_insert = list()
        for key in DICTIONARY_TABLE.keys():
            internal = DICTIONARY_TABLE [key]
            for index, entrance in enumerate(internal):
                size_value = len(entrance)-1
                prepare_statement = f'INSERT INTO {key} VALUES ('
                for depth ,n in enumerate(entrance):
                    if depth == size_value:
                        prepare_statement += f'{n} ) ;'
                    else:
                        prepare_statement += f' {n}, '
                list_insert.append(prepare_statement)
        return list_insert


"""TASK 0 METHOD UNION INTERSECT CARTESIAN """



" APPEND RESULT "

def append_result_cart_union_inter (list_message, list_result):
    for values in list_result:
        list_message.append(values)


" CALCULATION UNION "

def verify_union (dictionary_relation):
    list_message = list()
    sets_list = list(dictionary_relation.values())
    dictionary_union = dict()
    for value in sets_list:
        for internal_value in sets_list:
            union_set = value.union(internal_value).copy()
            if value.issubset(internal_value) or internal_value.issubset(value):
                continue
            dictionary_union[(sets_list.index(value), sets_list.index(internal_value))] = union_set

    for external_key in dictionary_union.keys():
        for internal_key in dictionary_relation.keys():
            if dictionary_union[external_key] == dictionary_relation[internal_key]:
                value_key_search = sets_list[external_key[0]]
                value_second_key_search = sets_list[external_key[1]]
                # VERIFY IF THEY WANT DUPLICATE
                message_return = f'{internal_key} {message_union}'
                for k in dictionary_relation.keys():
                    values_compare = dictionary_relation[k]
                    # SAVE GLOBALLY FOR TASK 1
                    if values_compare == value_key_search:
                        INDEX_CREATE_TABLE.append(k)
                        DICTIONARY_TABLE[k] = values_compare
                        message_return += f' {k}'
                    if values_compare == value_second_key_search:
                        DICTIONARY_TABLE[k] = values_compare
                        message_return += f' and {k}'
                        INDEX_CREATE_TABLE.append(k)
                list_message.append(message_return)
                # EVALUATE A BREAK
                return list_message
    return list_message


" CALCULATION INTERSECTION "

# EXTRACT THE VALUE
def verify_intersection(dictionary_relation):
    list_message = list()
    # VERIFY IF THERE IS ONLY ONE MESSAGE
    sets_list = list(dictionary_relation.values())
    dictionary_intersection = dict()
    for v in sets_list:
        for x in sets_list:
            if v.issubset(x) or x.issubset(v):
                continue
            result = v.intersection(x)
            if result:
                if result in dictionary_intersection.values():
                    continue
                dictionary_intersection[sets_list.index(v), sets_list.index(x)] = result
                break  # CANNOT HAVE MORE THAN ONE INTERSECTION
    for unpack in dictionary_intersection.keys():
        for internal_unpack in dictionary_relation.keys():
            if dictionary_intersection[unpack] == dictionary_relation[internal_unpack]:
                result_values = sets_list[unpack[0]]
                extra_result_values = sets_list[unpack[1]]
                # NAME TABLE
                message_result = f'{internal_unpack} {message_intersection}'
                # VERIFICATION AND EXTRACTION OF THE NAME TABLE
                # TABLE NAME IS NOT FIXED
                for k in dictionary_relation.keys():
                    values_compare = dictionary_relation[k]
                    if values_compare == result_values:
                        DICTIONARY_TABLE[k] = values_compare
                        INDEX_CREATE_TABLE.append(k)
                        message_result += f' {k}'
                    if values_compare == extra_result_values:
                        DICTIONARY_TABLE[k] = values_compare
                        INDEX_CREATE_TABLE.append(k)
                        message_result += f' and {k}'
                list_message.append(message_result)
    return list_message
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
    for firstKey, extv in enumerate(list_tuple):
        for intern in list_tuple:
         # CONSTRAINT SUBSET
         if extv.issubset(intern) or intern.issubset(extv) :
            continue
         dictionary_store_concat [firstKey, list_tuple.index(intern)]  = set_cartesian_product(list_tuple[firstKey], intern)
    # FROM END TO BEGIN
    for firstKey in range(until-1,-1,-1):
        for second_key in range (firstKey-1, -1, -1):
            if list_tuple[firstKey].issubset(list_tuple[second_key]) or list_tuple[second_key].issubset(list_tuple[firstKey]):
                continue
            dictionary_store_concat[firstKey, second_key] = set_cartesian_product(list_tuple[firstKey], list_tuple[second_key])
    # MISS CARLO RETURN THE MESSAGE
    return find_occurrence_cartesian(dictionary_store_concat,dictionary_relation, list_tuple)



# EXTRACT CARTESIAN PRODUCTION BETWEEN TUPLES
def set_cartesian_product(set_tuple_one, set_tuple_two)-> set:
    set_record = set()
    for external in set_tuple_one:
        for internal in set_tuple_two:
            concat = external + internal
            set_record.add(concat)
    return set_record

# VERIFICATION IF THERE IS A CARTESIAN
def find_occurrence_cartesian (dictionary_cartesian, original_dictionary, list_tuple)-> list:
    list_message = list()
    for k in dictionary_cartesian.keys():
        for ik in original_dictionary.keys():
            if dictionary_cartesian[k] == original_dictionary[ik]:
                message = f'{ik} {message_cartesian}'
                valueFirst = list_tuple[k[0]]
                valueSecond = list_tuple[k[1]]

                for control_key in original_dictionary.keys():
                    if original_dictionary[control_key] == valueFirst:
                        message +=f' {control_key}'
                        DICTIONARY_TABLE[control_key] = original_dictionary[control_key]
                        INDEX_CREATE_TABLE.append(control_key)
                    if original_dictionary[control_key] == valueSecond:
                        message += f' and {control_key}'
                        DICTIONARY_TABLE[control_key] = original_dictionary[control_key]
                        INDEX_CREATE_TABLE.append(control_key)
                list_message.append(message)
    return  list_message

