
"""
CREATE TABLE t22 ( c0 INTEGER , c1 INTEGER , c2 INTEGER , c3 INTEGER , c4 INTEGER , c5 INTEGER , c6 INTEGER  )
PASS THE LIST OF MESSAGE, AND THE LIST EXTRACTED
EXTRACTED KEY AND NUMBER OF VALUES
CREATE THE STATEMENT

"""

import unittest

class TestDictionary(unittest.TestCase):

    CREATE_TABLE_INDEX = list()


    def test_split_string (self):
        split_value = "t11 is UNION of t2 and t14"
        list_message = "t11 is UNION of t2 and t14"
        number = ""
        # THIS BECOME A LIST
        for key, value in enumerate(list_message):
           if not value.isdigit():
               split_value = split_value.replace(value,"")
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
                        "t5": {(8, 8, 9, 9), (4, 3, 0, 8), (3, 3, 4, 5), (8, 1, 7, 4), (4, 3, 0, 7), (3, 9, 10, 11) }
                        }

        sets_list = list(dictionary_p.values())
        dictionary_union = dict()
        for key_external, value in enumerate(sets_list[0:len(sets_list)-1]):
            for key_internal, internal_value in enumerate(sets_list[(key_external + 1):], start=key_external+ 1):
                union_set = value.union(internal_value).copy()
                # VERIFICATION NO SUBSET
                if value.issubset(internal_value) or internal_value.issubset(value):
                    continue
                    # UNION REMOVE DUPLICATE ROW
                dictionary_union[(key_external,key_internal)] = union_set

        for external_key in dictionary_union.keys():
            for internal_key in dictionary_p.keys():
                if dictionary_union[external_key] == dictionary_p[internal_key]:
                  print(f'\n {internal_key} is UNION of t{external_key[0]} and t{external_key[1]}')
                  self.CREATE_TABLE_INDEX.append(external_key)

        self.create_statement(dictionary_p)

    def create_statement(self, dictionary_p):
        list_keys = list()
        for values in self.CREATE_TABLE_INDEX:
            table_one = 't'+str(values[0])
            table_two = 't'+str(values[1])
            list_keys.append(table_one)
            list_keys.append(table_two)
    # PREPARE STATEMENT

        for extract_key in list_keys:
            prepare_statement = f'CREATE TABLE'
            # EXTRACT THE SIZE OF THE TUPLE
            size = len (dictionary_p [extract_key])
            prepare_statement+=f' {extract_key} ('
            print(f'extract key {size} ')
            for n in range(0, size+1):
                if size == n:
                    prepare_statement +=f' c{n} INTEGER )'
                else:
                    prepare_statement += f' c{n} INTEGER, '

            print(f'{prepare_statement}')

"""
CREATE TABLE t22 ( c0 INTEGER , c1 INTEGER , c2 INTEGER , c3 INTEGER , c4 INTEGER , c5 INTEGER , c6 INTEGER )


"""




