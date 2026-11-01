import numpy as np
from itertools import product
from architecture import Block, Network, ScaleBlock, OutputBlock, Sigmoid
from pythonPack.numpy.neural_network.asses.dataloader import Dataloader

# TRAINABLE WEIGHT
class Dense(Block):
# ADD FUNCTION UPDATE CARLO 1
    """Fully connected layer: o = W i + b, with W of shape (m, n), b of shape (m,)."""
    # BUILD THE NEURON
    def __init__(self, neuron, dimension, name=None, rng=None):
        super().__init__(name)
        # Pseudo number generator
        rng = rng or np.random.default_rng()
        self.m, self.n = neuron, dimension
        # Scaled init keeps the induced local fields at a reasonable magnitude
        # draw random samples from a normal (Gaussian) distribution.
        self.Weigth = rng.normal(0.0, 1.0 / np.sqrt(dimension), size=(neuron, dimension))
        self.bias = np.zeros(neuron)
        # CARLO THIS VARIABLE ARE USED TO STORED THE WEIGHT AND THE GRADIENT
        self.grad_W = np.zeros_like(self.Weigth)
        self.grad_b = np.zeros_like(self.bias)
    # FORWARD PROPAGATION
    def forward(self, x):
        # x: (n,) or (batch, n)  ->  (m,) or (batch, m)
        self.forward_in = x
        # print(x)
        # MULTIPLY CARLO WITH THE WEIGHT AND PLUAS B
        self.forward_out = x @ self.Weigth.T + self.bias
        # print(self.forward_out)
        return self.forward_out
    # BACKWARD PROPAGATION
    def backward(self, grad):
        # grad = dL/do, same shape as forward_out. Returns dL/di.
        self.backward_in = grad
        x = np.atleast_2d(self.forward_in)
        g = np.atleast_2d(grad)
        # TRANSPOSE ARRAY self.W.T
        self.grad_W = g.T @ x             # dL/dW, shape (m, n)
        # SUM GIVE ARRAY
        self.grad_b = g.sum(axis=0)       # dL/db, shape (m,)
 
        # Uses the weights from the forward pass: update() has not run yet
        self.backward_out = (g @ self.Weigth).reshape(np.shape(self.forward_in))
        return self.backward_out


    def update_weigth_with_gradient_descendent(self, learning_rate):
        self.Weigth -= learning_rate * self.grad_W
        self.bias-= learning_rate * self.grad_b


if __name__ == '__main__':
     # LAYERS SET UP NETWORK
     layers = [ScaleBlock(1.0), OutputBlock('output')]
     network = Network('test', layers, 0.01)
     dense_autoencoder = Dense(3,4  )
     # YOU USE TO  CALCULATE THE COMBINTAION
     data_loader = Dataloader()
     # CREATIONG MATRIX 4 RAW AND 4 COLUMNS SUBTITUE DATA LOADER
     input_layer = np.zeros((4,4))
     # POSSIBLE COMBINATION
     combinations = (list(product([0, 1], repeat=4)))
     for x, y in enumerate(combinations):
         input_layer[x:] = y

      # NEURON CALCULATION FIRST WEIGTH
     for x, y in enumerate(combinations):
         input_layer[x:] = y
     # MYSTERY TASK FOUR
     # print(dense_autoencoder.forward(input_layer))
     # FORWARD RESULT FIRST LAYER
     sigmoid = Sigmoid("pippo")
     for i, im in enumerate(input_layer):
           print(f'input_layer  {im}')
           pre_network_layer = dense_autoencoder.forward(im)
           print(f'pre_network out  {pre_network_layer}')
           # TAKE THE OUTPUT OF THE PREVIOUS LAYER
           # fw = network.forward(forward_out)
           # print(f'move is {fw}')
           network_layer_prediction = sigmoid.forward(pre_network_layer)
           print(f'output network prediction {network_layer_prediction}')

           # error = sigmoid.backward(network_layer_prediction)
           # print(f'error {network_layer_prediction}')



     #
     #
     # backward_out = dense_autoencoder.backward(forward_out)
     #
     # for i, im in enumerate(input_layer):
     #     fw = network.forward(im)
     #
     #     backward = network.backward(im - fw)
     #
     #     if i > 20:
     #         break

     """"
     I found that the network layer is unslees becasue Block class does not keep 
in the memory the network operations related to the various input layer. Th 
ere is always a override that self.input and self.out. Further, the Scale bl
ock does not match the scale factor in the Dense class

     
     https://d2l.djl.ai/chapter_multilayer-perceptrons/mlp.html
     
     """



