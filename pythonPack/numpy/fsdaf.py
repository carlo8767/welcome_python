from itertools import product
import numpy as np
import matplotlib as mp
from matplotlib.pyplot import plot

from itertools import product

from numpy.testing.print_coercion_tables import print_new_cast_table
# NINE RAW AND 2 COLUM
_trainingset = np.zeros([10, 2])
print(_trainingset.shape)
# n power of n
weightArray = np.array(list((product([0, 1,0,1,2], repeat=2))))
for x, v in enumerate(weightArray):
    _trainingset[x:] = v


    class SquaredEuclideanLoss(Block):

        def forward_eclidan(self, pred, target):
            for x in pred:
                error = (x - target) ** 2
                super().error_euclidian(error)