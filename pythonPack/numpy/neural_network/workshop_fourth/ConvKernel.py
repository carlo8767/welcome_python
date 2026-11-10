import numpy as np

from pythonPack.numpy.neural_network.workshop_fourth.architecture import Block


class ConvKernel(Block):


    list_forward_in: np.array = None
    list_backward_out: np.array = None


    def __init__(self, name,kernel_size):
        super().__init__(name)
        self.kernel_size = int(kernel_size) # VERIFY WHY ODD
        self.weight_matrix = np.zeros((self.kernel_size,self.kernel_size))
        self.list_forward_in = list()


    def forward_pass(self, input_in:np.array, kernel:np.array):
        # STRIDE
        strid_shift = 0
        limit_vertical_input, limit_hor_input = np.shape(input_in)
        limit_vertical_kernel, limit_hor_kernel = np.shape(kernel)
        for p in range(0,limit_vertical_input):
            for m in range(0,limit_hor_input):
                s = input_in[p].flat[m:limit_hor_kernel]
                self.forward_in = np.multiply(kernel, s).sum()
                limit_hor_kernel+=1
                if limit_hor_kernel> limit_hor_input:
                    break
            limit_hor_kernel = limit_vertical_kernel




        for y in range(0,limit_vertical_input):
            s = input_in.flat[strid_shift:limit_hor_kernel]
            self.forward_in = np.multiply(kernel, s).sum()
            self.list_forward_in.append(self.forward_in)
            strid_shift+=1
            limit_hor_kernel+=1
        return self.list_forward_in


