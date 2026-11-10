
import pytest
import numpy as np
from pythonPack.numpy.neural_network.workshop_fourth.ConvKernel import ConvKernel

class TestConvKernel:


    def test_forward_pass(self):
        cv = ConvKernel("",int(3) )
        input_v = np.arange(25).reshape(5,5)
        # USE THIS FOR THE STRIDE
        sf = input_v.flat[1:5]
        kernel = np.arange(9).reshape(3,3)

        # ALL RAW AND THE SECOND COLUM
        res = cv.forward_pass(input_v, kernel)
        assert res == [5, 14, 23]

