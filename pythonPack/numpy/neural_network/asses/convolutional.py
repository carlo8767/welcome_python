import numpy as np
from itertools import product, repeat


pixel = np.array([[0,1,0,1], [1,1,0,1],[0,1,1,1],[0,1,0,0]])
print(pixel)
# BEFORE AND AFTER, mode different modes replace, such as edge!!
padding_zero = np.pad(pixel, [1,1] , mode="constant", constant_values=0)
print(padding_zero)
print(padding_zero.shape)
kernel_filter_zero_padding = np.zeros((6,6))
convolutional_multiplicaiton = np.convolve(padding_zero, kernel_filter_zero_padding, mode="full")
