from typing import List

import numpy as np

from architecture import Block


## From Last Weeks Solution

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

    def update(self, learning_rate):
        pass


## Week 3

class Network(Block):
    '''Task 1'''

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

    # TASK 1.1 UPDATE WEIGHT
    def update(self, learning_rate):

        for block in reversed(self.layers):
            block.update(learning_rate)


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


class Dense(Block):
    """Fully connected layer: o = W i + b, with W of shape (m, n), b of shape (m,)."""

    def __init__(self, m, n, name=None, rng=None):
        super().__init__(name)
        rng = rng or np.random.default_rng()
        self.m, self.n = m, n
        # Scaled init keeps the induced local fields at a reasonable magnitude
        self.W = rng.normal(0.0, 1.0 / np.sqrt(n), size=(m, n))
        self.b = np.zeros(m)
        self.W_grad = np.zeros_like(self.W)
        self.b_grad = np.zeros_like(self.b)

    def forward(self, x):
        # x: (n,) or (batch, n)  ->  (m,) or (batch, m)
        self.forward_in = x
        self.forward_out = x @ self.W.T + self.b
        return self.forward_out

    def backward(self, grad):
        # grad = dL/do, same shape as forward_out. Returns dL/di.
        self.backward_in = grad
        x = np.atleast_2d(self.forward_in)
        g = np.atleast_2d(grad)

        self.W_grad = g.T @ x  # dL/dW, shape (m, n)
        self.b_grad = g.sum(axis=0)  # dL/db, shape (m,)

        # Uses the weights from the forward pass: update() has not run yet
        self.backward_out = (g @ self.W).reshape(np.shape(self.forward_in))
        return self.backward_out

    # TASK 1.1 UPDATE WEIGHT
    def update(self, learning_rate):
        self.W -= learning_rate * self.W_grad
        self.b -= learning_rate * self.b_grad


# TASK TWO
class SquaredEuclideanLoss:
    loss: np.array = None
    pred: np.array = None
    target: np.array = None

    def forward(self, pred, target):
        # CALCULATE EUCLIDIANTE
        self.loss = (pred - target) ** 2
        self.pred = pred
        self.target = target

        # REMEBER TO RETURN THE LOSS !!
        return np.sum(self.loss)

    def backward(self):
        # ERROR SIGNAL

        error_signal = 2 * (self.pred - self.target)
        return error_signal


# TASK THREE
denseblock = Dense(3, 10, 'denseblock')

autoencoder = Network('autoencoder', [Dense(3, 4), Dense(4, 3)], 1.0)
loss = SquaredEuclideanLoss()


