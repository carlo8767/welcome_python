
import numpy as np
import matplotlib as mp
from matplotlib.pyplot import plot

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
two_dimensional = np.array([[1,2][0,1]])
two_dimensional = np.array([[1, 2, 3], [0, 9, 8]])
print(two_dimensional)
print(two_dimensional[0][1])
print(two_dimensional.shape)




