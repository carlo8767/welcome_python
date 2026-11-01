from dataloader import Dataloader
from pythonPack.numpy.neural_network.asses.architecture import ScaleBlock, OutputBlock, Network
import numpy as np
from itertools import product


if __name__ == '__main__':
    # https://classic.d2l.ai/chapter_deep-learning-computation/model-construction.html

    layers = [ScaleBlock(1.0), OutputBlock('output')]
    network = Network('test', layers, 0.01)

    loader = Dataloader()

    input_layer = np.zeros((2, 2))
    # POSSIBLE COMBINATION
    combinations = (list(product([0, 1], repeat=2)))
    for x, y in enumerate(combinations):
        input_layer[x:] = y

    # NEURON CALCULATION FIRST WEIGTH
    for x, y in enumerate(combinations):
        input_layer[x:] = y


    for i, im in enumerate(input_layer):
        fw = network.forward(im)

        network.backward(im-fw)

        if i>3:
            break



    #
    # for i, im in enumerate(loader.training_set()):
    #     fw = network.forward(im)
    #
    #     network.backward(im-fw)
    #
    #     if i>20:
    #         break
