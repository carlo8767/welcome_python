from typing import List

import numpy as np

## From Last Weeks Solution

class Block:
# ADD FUNCTION UPDATE CARLO 1
    forward_in: np.array = None
    forward_out: np.array = None

    backward_in: np.array = None
    backward_out: np.array = None

    def __init__(self, name):
        self.name = name

    def forward(self, input: np.array) -> np.array:
        '''Implements the identity function. Input = output'''
        self.forward_in = input
        self.forward_out = input
        return input

    def backward(self, error: np.array) -> np.array:
        self.backward_in = error
        self.backward_out = error
        return error


class ScaleBlock(Block):
    '''I wrote a block that can implement both required blocks by setting the right parameter'''

    def __init__(self, scaling_factor):
        super().__init__(f'Scale Block with factor {scaling_factor}')
        self.scaling_factor = scaling_factor

    def forward(self, input):
        super().forward(input)
        self.forward_out = self.scaling_factor * input
        return self.forward_out


class OutputBlock(Block):

    def forward(self, input):
        super().forward(input)
        print(input)
        return input


## Week 3

class Network(Block):
    '''Task 1'''
# ADD FUNCTION UPDATE CARLO TASK 1
    def __init__(self, name, layers: List[Block], learning_rate: float):
        super().__init__(name)

        self.layers = layers
        self.learning_rate = learning_rate


    def forward(self, input):
        self.forward_in = input

        x = input
        for block in self.layers:
            x = block.forward(x)

        self.forward_out = x
        return x


    def backward(self, error):
        super().backward(error)

        x = error
        for block in reversed(self.layers):
            x = block.backward(x)

        self.backward_out = x
        return x


class Sigmoid(Block):
    '''Task 3'''

    def forward(self, input):
        super().forward(input)
        self.forward_out = 1. / (1. + np.exp(-input))
        return self.forward_out

    def backward(self, error):
        super().backward(error)
        self.backward_out = error * (1. - error)
        return self.backward_out
