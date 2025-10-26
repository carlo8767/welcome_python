from speechd_config import Tests

import is_prime as prime

import unittest

import matplotlib.pyplot as plt
import numpy as np
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


      # Original unit square corners
      square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T  # 2x5

      # Transformation matrix
      A = np.array([[2, 1],
                    [1, 3]])

      # Transformed corners
      transformed = A @ square

      # Plot
      plt.figure(figsize=(6, 6))
      plt.plot(square[0], square[1], 'b-', label='Original square')
      plt.plot(transformed[0], transformed[1], 'r-', label='Transformed parallelogram')
      plt.quiver(0, 0, 2, 1, angles='xy', scale_units='xy', scale=1, color='g', label='A*i')
      plt.quiver(0, 0, 1, 3, angles='xy', scale_units='xy', scale=1, color='orange', label='A*j')
      plt.xlim(-1, 5)
      plt.ylim(-1, 5)
      plt.grid(True)
      plt.legend()
      plt.title('Unit square transformed by matrix A')
      plt.show()




