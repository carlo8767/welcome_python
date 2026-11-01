

import numpy as np
from itertools import product
from typing import List



class Block:
    forward_in: np.array = None
    forward_out: np.array = None

    backward_in: np.array = None
    backward_out: np.array = None

    W: np.array = None
    b: np.array = None




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

    def update(self, learning_rate):
        self.W -= learning_rate * self.W_grad
        self.b -= learning_rate * self.b_grad



class Network(Block):

    def __init__(self, name, layers: List[Block], learning_rate: float):
        super().__init__(name)

        self.layers = layers
        self.learning_rate = learning_rate


    def forward(self, input):
        self.forward_in = input

        x = input
        for block in self.layers:
            # HERE CALL THE DENSE BLOCK
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

    def update(self, learning_rate):
        for block in reversed(self.layers):
            block.update(learning_rate)

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

class SquaredEuclideanLoss():

    loss_function: np.array = None
    prediction: np.array = None
    target: np.array = None


    def __init__(self, name):
        self.name=name

    def forward (self, pred, target):
        self.loss_function = (pred - target)**2
        self.target = target
        self.prediction = pred
        return np.sum(self.loss_function)



    def backward(self):
        # DERIVATIVE
        backward_out = 2 * (self.prediction - self.target)
        return backward_out



if __name__ == '__main__':
    # define size of the ouput the multiplication
    # BECAUSE TRANSPOSE
    # CREATION WEIGTH LAYER
    denseblock = Dense(3,10)


    # CREATION TRAINING DATA
    input_layer = np.zeros((4, 10))
    # POSSIBLE COMBINATION
    combinations = (list(product([0, 1,], repeat=10)))
    for x, y in enumerate(combinations[:4]):
         input_layer[x] = y
    # CALL THE OUTPUT AND PASS THE WEIGHT
    layers = [denseblock , OutputBlock('output')]

    print(input_layer)
    n = Network("test", layers, 1.0)
    # PASS THE TRAINING AND CALL INHERITANCE
    pred = n.forward(input_layer)
    print(pred)

    l = SquaredEuclideanLoss("square")
    y = np.arange(1,13).reshape(4,3)
    # TASK 2.1
    l_value = l.forward(pred,y)
    print("euc",l_value)
    n.backward(l.backward())

    #TASK  AUTOENCODER
    d_one = Dense(3,4)
    d_two = Dense(4, 3)

    autoencoder = Network("autoencoder", [d_one, d_two], 1.0)
    loss = SquaredEuclideanLoss("loss")






    """"
    The idea is behind that the Dense Block take in account the creation of the weight
    that will define the output. The input for the dense block is composed by
    m and n. M is the output and n is the dimension. Why? That is not clear
    Additnoally the network layer work as a trigger for the forward pass, backprogation
    and update of the weigth    
    
    
    """



