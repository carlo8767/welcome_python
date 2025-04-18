import unittest
from os.path import split


class TestExercise(unittest.TestCase):


    def test_len_literals(self):
        # LITERAL EXPRESSION
        literal_list = [1, 2, 1, 3, 1, 4]
        set_literal_list = {1,2,1,3,1,4}
        size_set  = len(set_literal_list)
        size_list = len(literal_list)
        self.assertEqual(6, size_list)
        self.assertEqual(4, size_set)
        # CREATE A SET WITHOUT LITERAL
        set_one_to_ten = set(range(1,11))
        set_verification = {1,2,3,4,5,6,7,8,9,10}
        self.assertSetEqual(set_verification, set_one_to_ten)

    def test_set(self):
        input_string = "I like Sets and sets And dictionaries"
        # IF YOU SPLIT WITH SET IS NOT ORDER
        set_word = set(input_string.split())
        set_verify = {'I', 'like', 'And', 'dictionaries', 'sets', 'Sets', 'and'}
        self.assertSetEqual(set_verify, set_word)
        # LOWER WORD
        set_lower = set(input_string.lower().split())
        for i, v in enumerate(set_lower, 1):
          print(f'{i}: {v}')

    def test_convert_input(self):
      input_value = str(input("Enter a value\n"))
      set_word = set(input_value.split())
      set_verify = {'Hello', 'Set'}
      self.assertSetEqual(set_verify, set_word)















