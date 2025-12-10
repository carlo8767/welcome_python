"""
CREATE TABLE t22 ( c0 INTEGER , c1 INTEGER , c2 INTEGER , c3 INTEGER , c4 INTEGER , c5 INTEGER , c6 INTEGER  )
PASS THE LIST OF MESSAGE, AND THE LIST EXTRACTED
EXTRACTED KEY AND NUMBER OF VALUES
CREATE THE STATEMENT

"""

import unittest

from sympy import true

INDEX_CREATE_TABLE = list()
DICTIONARY_TABLE = dict()
message_cartesian = "is CARTPROD of"
message_no_match = "NO MATCH"
message_intersection = "is INTERSECTION of"
message_union = "is UNION of"
list_insert_db = list()


class TestDictionary(unittest.TestCase):
    CREATE_TABLE_INDEX = list()
    DICTIONARY_TABLE = dict()

    def test_append(self):
        list_state = list()
        statement = 'CREATE TABLE t8 ( c0 INTEGER,  c1 INTEGER,  c2 INTEGER,  c3 INTEGER,  c4 INTEGER,  c5 INTEGER,  c6 INTEGER,  c7 INTEGER,  c8 INTEGER )'
        list_state.append(statement)
        for s in list_state:
            print(s)

    def test_split_string(self):
        split_value = "t11 is UNION of t2 and t14"
        list_message = "t11 is UNION of t2 and t14"
        number = ""
        # THIS BECOME A LIST
        for key, value in enumerate(list_message):
            if not value.isdigit():
                split_value = split_value.replace(value, "")
                continue
            for values in list_message[key:]:
                if values.isdigit():
                    values.join(number)
                else:
                    break

    def test_unpacking_union_second(self):
        dictionary_p = {"t0": {(3, 3, 7, 8), (4, 3, 4, 1), (3, 3, 9, 8)},
                        "t1": {(3, 3, 7, 8), (4, 3, 4, 1), (3, 3, 9, 8), (9, 8, 8, 8), (4, 3, 1, 1), (3, 3, 0, 5)},
                        "t2": {(9, 8, 8, 8), (4, 3, 1, 1), (3, 3, 0, 5)},
                        "t3": {(8, 8, 9, 9), (4, 3, 0, 8), (3, 3, 4, 5)},
                        "t4": {(8, 1, 7, 4), (4, 3, 0, 7), (3, 9, 10, 11)},
                        "t5": {(8, 8, 9, 9), (4, 3, 0, 8), (3, 3, 4, 5), (8, 1, 7, 4), (4, 3, 0, 7), (3, 9, 10, 11)}
                        }

        sets_list = list(dictionary_p.values())
        dictionary_union = dict()
        for key_external, value in enumerate(sets_list[0:len(sets_list) - 1]):
            for key_internal, internal_value in enumerate(sets_list[(key_external + 1):], start=key_external + 1):
                union_set = value.union(internal_value).copy()
                # VERIFICATION NO SUBSET
                if value.issubset(internal_value) or internal_value.issubset(value):
                    continue
                    # UNION REMOVE DUPLICATE ROW
                dictionary_union[(key_external, key_internal)] = union_set

        for external_key in dictionary_union.keys():
            for internal_key in dictionary_p.keys():
                if dictionary_union[external_key] == dictionary_p[internal_key]:
                    print(f'\n {internal_key} is UNION of t{external_key[0]} and t{external_key[1]}')
                    self.CREATE_TABLE_INDEX.append(external_key)
                    keys_one = f't{str(external_key[0])}'
                    keys_two = f't{str(external_key[1])}'
                    self.DICTIONARY_TABLE[keys_one] = dictionary_p[keys_one]
                    self.DICTIONARY_TABLE[keys_two] = dictionary_p[keys_two]

        self.create_statement(dictionary_p)
        self.insert_statement()

    def create_statement(self, dictionary_p):
        list_keys = list()
        list_statement = list()
        for values in self.CREATE_TABLE_INDEX:
            table_one = 't' + str(values[0])
            table_two = 't' + str(values[1])
            list_keys.append(table_one)
            list_keys.append(table_two)
        # PREPARE STATEMENT

        for extract_key in list_keys:
            # EXTRACT THE SIZE OF THE TUPLE
            size_insert_value = dictionary_p[extract_key]
            for p in size_insert_value:
                prepare_statement = f'CREATE TABLE'
                size = len(p)
                prepare_statement += f' {extract_key} ('
                print(f'extract key {size} ')
                for n in range(0, size):
                    if size - 1 == n:
                        prepare_statement += f' c{n} INTEGER );'
                    else:
                        prepare_statement += f' c{n} INTEGER, '
                list_statement.append(prepare_statement)
                break

            print(f'{list_statement}')

    def insert_statement(self):
        list_insert = list()
        for key in self.DICTIONARY_TABLE.keys():
            internal = self.DICTIONARY_TABLE[key]
            for index, entrance in enumerate(internal):
                size_value = len(entrance) - 1
                prepare_statement = f'INSERT INTO {key} VALUES ('
                for depth, n in enumerate(entrance):
                    if depth == size_value:
                        prepare_statement += f'{n} )'
                    else:
                        prepare_statement += f' {n}, '
                list_insert.append(prepare_statement)


" CALCULATION INTERSECTION "


# EXTRACT THE VALUE
def test_verify_intersection():
    dictionary_relation = {'t7': {(1, 2), (3, 4)},
             't15': {(5, 6), (3, 4)},
             't17': {(1, 2), (3, 4), (5, 6)},
             't2': {(30, 40), (10, 20)},
             't3': {(50, 60), (30, 40)},
             't11': {(30, 40)},
             't9': {(7,), (8,)},
             't21': {(11,), (9,), (10,)},
             't24': {(7, 10), (8, 10), (7, 9), (8, 9), (7, 11), (8, 11)},
             't_extra1': {(100, 200), (300, 400)},
             't_extra2': {(999,), (1000,)}}

    # EXTRACT THE VALUE
    print(f'{dictionary_relation}')
    list_message = list()
    # VERIFY IF THERE IS ONLY ONE MESSAGE
    sets_list = list(dictionary_relation.values())
    dictionary_interset = dict()
    for  v in sets_list:
        print(f'v is .. {v}')
        for x in sets_list:
            if v.issubset(x) or x.issubset(v):
                continue
            result = v.intersection(x)
            if result:
                if result in dictionary_interset.values():
                    continue
                dictionary_interset[sets_list.index(v), sets_list.index(x)] = result
                break  # CANNOT HAVE MORE THAN ONE INTERSECTION
    for unpack in dictionary_interset.keys():
        for internal_unpack in dictionary_relation.keys():
            if dictionary_interset[unpack] == dictionary_relation[internal_unpack]:
                result_values = sets_list[unpack[0]]
                extra_result_values = sets_list[unpack[1]]
                # NAME TABLE
                message_result = f'{internal_unpack} {message_intersection}'

                for k in dictionary_relation.keys():
                    values_compare = dictionary_relation[k]
                    if values_compare == result_values:
                        DICTIONARY_TABLE[k] = values_compare
                        INDEX_CREATE_TABLE.append(k)
                        message_result+= f' {k}'
                    if values_compare == extra_result_values:
                        DICTIONARY_TABLE[k] = values_compare
                        INDEX_CREATE_TABLE.append(k)
                        message_result += f' and {k}'
                list_message.append(message_result)
    return list_message



def test_union():
    # IT THERE ARE MULTLE UNION DOES NOT WORK
    dictionary_relation = {'t7': {(1, 2), (3, 4)},
                           't15': {(5, 6), (3, 4)},
                           't17': {(1, 2), (3, 4), (5, 6)},
                           't2': {(30, 40), (10, 20)},
                           't3': {(50, 60), (30, 40)},
                           't11': {(30, 40)},
                           't9': {(7,), (8,)},
                           't21': {(11,), (9,), (10,)},
                           't24': {(7, 10), (8, 10), (7, 9), (8, 9), (7, 11), (8, 11)},
                           't_extra1': {(100, 200), (300, 400)},
                           't_extra2': {(999,), (1000,)}}

    list_message = list()
    sets_list = list(dictionary_relation.values())
    dictionary_union = dict()
    for value in sets_list:
        for internal_value in sets_list:
            union_set = value.union(internal_value).copy()
            if value.issubset(internal_value) or internal_value.issubset(value):
                continue
            dictionary_union[(sets_list.index(value), sets_list.index(internal_value))] = union_set

    for external_key  in dictionary_union.keys():
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





def test_verification_cartesian()-> list:
    # ITERATE OVER A SET OF LIST WITH INDEX

    dictionary_relation = {'t7': {(1, 2), (3, 4)},
                           't15': {(5, 6), (3, 4)},
                           't17': {(1, 2), (3, 4), (5, 6)},
                           't2': {(30, 40), (10, 20)},
                           't3': {(50, 60), (30, 40)},
                           't11': {(30, 40)},
                           't9': {(7,), (8,)},
                           't21': {(11,), (9,), (10,)},
                           't24': {(7, 10), (8, 10), (7, 9), (8, 9), (7, 11), (8, 11)},
                           't_extra1': {(100, 200), (300, 400)},
                           't_extra2': {(999,), (1000,)}}

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


def test_create_statement():
    INDEX_CREATE_TABLE = ['i1', 'i2', 'c1', 'c2', 'u1', 'u2']
    DICTIONARY_TABLE = {'i1': {(3, 7), (2, 6), (1, 5)}, 'i2': {(3, 7), (5, 9), (4, 8)}, 'c1': {(2,), (4,)},
                        'c2': {(6,), (8,)}, 'u1': {(11, 22), (33, 44)}, 'u2': {(55, 66), (33, 44)}}
    list_statement = list()
    for extract_key in INDEX_CREATE_TABLE:
        # EXTRACT THE SIZE OF THE TUPLE
        size_insert_value = DICTIONARY_TABLE[extract_key]
        for p in size_insert_value:
            prepare_statement = f'CREATE TABLE'
            size = len(p)
            prepare_statement+=f' {extract_key} ('
            for n in range(0, size):
                if size-1 == n:
                    prepare_statement +=f' c{n} INTEGER ) ;'
                else:
                    prepare_statement += f' c{n} INTEGER, '
            list_statement.append(prepare_statement)
            break
    return  list_statement












def test_intersss():
    se = [{(1, 2), (3, 4)}, {(3, 4), (5, 6)}, {(1, 2), (3, 4), (5, 6)}, {(10, 20), (30, 40)}, {(30, 40), (50, 60)},
          {(30, 40)}, {(7,), (8,)}, {(9,), (10,), (11,)}, {(7, 9), (7, 10), (7, 11), (8, 9), (8, 10), (8, 11)},
          {(100, 200), (300, 400)}, {(999,), (1000,)}]

    print(se[0].issubset(se[1]))


"""
CREATE TABLE t22 ( c0 INTEGER , c1 INTEGER , c2 INTEGER , c3 INTEGER , c4 INTEGER , c5 INTEGER , c6 INTEGER )
INSERT INTO users
VALUES (NULL, 'Alice', 'alice@example.com', 30);


"""
