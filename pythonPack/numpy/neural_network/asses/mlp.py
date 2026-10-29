from dataloader import Dataloader
from pythonPack.numpy.neural_network.asses.architecture import ScaleBlock, OutputBlock, Network

if __name__ == '__main__':


    layers = [ScaleBlock(1.0), OutputBlock('output')]
    network = Network('test', layers, 0.01)

    loader = Dataloader()

    for i, im in enumerate(loader.training_set()):
        fw = network.forward(im)

        print(network.backward(im-fw))

        if i>20: 
            break
