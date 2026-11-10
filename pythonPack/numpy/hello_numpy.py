from itertools import product
import numpy as np
import matplotlib as mp
from matplotlib.pyplot import plot

from itertools import product

from numpy.testing.print_coercion_tables import print_new_cast_table

access_np = [[1,2,3],[4,5,6]]
print(np.shape(access_np))
print(access_np)

# multidimension with two axis and three
axis_dimension = [[1., 0., 0.], [0., 1., 2.], [0., 1., 2.]]

dimesion = np.shape(axis_dimension)
# NUMBER OF ELEMENT CONTAINS EQUALS TO THE PRODCUT OF THE TWO AXIS
size = np.size(axis_dimension)

print(size)

# CREATIONG np from an array or tuple

tuple_array = (3,4,5)
types = np.array(tuple_array)
print(type(types))

# CREATION ARRAY WITH A SPECIF MATRIX
a = np.arange(6).reshape(3,2)
print("The matrix is ", a)
# raw and colums
print(a[2,0])

print(a[0:3,1])



# PRINT AN ND ARRAY
new_array = np.arange(1,21).reshape(4,5)
print()
for raw in  new_array:
    print(raw)

for raw_flat in  new_array.flat:
    print(raw_flat)

# creation of diagonal matrix ( identity matrix)
print(np.eye(10))

# DOT PRODCUT
# first axis 1 and second 2

second_matrix = [[3,5]]
first_matrix = [[2,3], [1,2]]
print(np.dot(second_matrix, first_matrix))





a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 5]])
print(np.matmul(a,b))
print(b[0,1])

# CREATE AN ARRAY OF 1 GIVEN SPACE
ls = np.ones((5))
print(type(ls))
values = np.arange(1,7).reshape(2,3)
print(values)


# TWO DIMENSIONAL NP ARRAY
two_dimensional = np.array([[1, 2, 3], [0, 9, 8]])
print(two_dimensional)
# print(two_dimensional[0][1])
# print(two_dimensional.shape)
#
#
# # NP ZERO VERY NICE
# np_zero = np.zeros((16,4))



def yields_generator():
    for x in range(0,5):
        yield x


keep_alive = yields_generator()
print(next(keep_alive))
print(next(keep_alive))

def generators():
      return  np.random.default_rng()

# PSEUDO NUMBER GENERATOR
keep_alive = generators()
print(keep_alive)

# Define two matrices as NumPy arrays
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Perform matrix multiplication using the "@" operator
result = matrix_a @ matrix_b
print(result)

# SUM ARRAY FOR A GIVEN AXIS
sum_array = np.sum(matrix_a, axis=0)
print(sum_array)


arr = np.arange(24).reshape(2, 3, 4)
# CREATE ARRAY WITH A SPECIFIC VALUE AND DIMENSION
values = np.array(([0,1],[0,1],[0,1],[0,1]))
st = np.array(list(product(values)))
print(st.shape)
print(arr)
# VERY IMPORTANT BECAUSE THE INPUT I DO NOT KNOW WHAT WILL ASK
ns = np.zeros((4,4))
combinations = (list(product([0, 1], repeat=4)))
for x, y in enumerate(combinations):
    ns[x:]= y
print(ns)


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr.shape)
print(arr[0, 2:5])


np_array = np.array([[0,1],[1,0],[1,1]])
print(np_array.shape)

# cartesian product
combinations = (list(product([0, 1], repeat=3)))
print(combinations)

#NUMBER DIMENSION
z = np.zeros([10,10])
print(z.ndim)  # 2
print(z.shape) # (1, 3)

_trainingset = np.zeros([3, 10])
print(_trainingset)
for i, im in enumerate(np.array(list(product([0, 1])))):
    _trainingset[i, :] = im

new_array = np.arange(1,7).reshape(2,3)
print(new_array)


one_pred = np.arange(1,7).reshape(2,3)

two_target = np.arange(7,13).reshape(2,3)

sum_diff = np.zeros(two_target.shape)

values = (one_pred - two_target)**2


for x,y in enumerate(one_pred):
    print("access", two_target[x])
    print("y", y)
    sum_diff [x] = np.sum((y-two_target[x]) ** 2)


    def forward_variation(self, pred, target):

        # STORED THE LOSS FUNCTION
        m, n = (np.shape(pred))
        self.loss_function = np.zeros((int(m),int(n)))
        self.prediction = pred
        self.target = target
        for x,y in enumerate(pred):
            self.loss_function [x] = np.sum((y - target[x])**2)

        self.forward_out = self.loss_function
        return self.forward_out
print(type(sum_diff))

# WISE MULTIPLICAITON
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
print(np.multiply(x1, x2))


f = np.arange(8).reshape(4,2)
s = f.flat[1:3]
print(s)




