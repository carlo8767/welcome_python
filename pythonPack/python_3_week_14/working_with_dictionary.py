import unittest


DICTIONARY = {"Hello": "Ciao", "Goodbye": "Arrivederci", "University": "Università,",
             "Computer": "Computer", "Dictionary": "Dizionario"}

class Test_working_dictionary (unittest.TestCase):


  def test_words (self):

    for k,v in DICTIONARY.items():
        values = k+v
        self.assertEqual("HelloCiao", values)
        print(f'The translation of {k} is {v}')
        break

  def test_translation_sorted (self):
      for k, v in sorted(DICTIONARY.items(), key = lambda t: t[1]):
          print(f'The translation of {k} is {v}')


  def test_parse_input(self):
      listNames = {"N": 1, "P":3}
      map()
