from speechd_config import Tests

import is_prime as prime

import unittest


class TestSum(unittest.TestCase):



  def test_is_prime (self):
    case_one = 11 * 17
    case_two = 2971215073
    case_three = 10203501230
    result = prime.is_prime(case_two)
    self.assertEqual(result, True)
    result = prime.is_prime(case_one)
    self.assertEqual(result, False)
    result = prime.is_prime(case_three)
    self.assertEqual(result, False, f'The number {case_three} it should be False')

  def test_list_is_prime (self):
    case_one = 11 * 17
    list_result = prime.smaller_prime_number(case_one)
    list_value = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    self.assertListEqual(list_result, list_value)


