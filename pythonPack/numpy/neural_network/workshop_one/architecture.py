import numpy as np

## Task 2

class Block:

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

