import numpy as np
from itertools import product


## Task 3

class Dataloader:

    def __init__(self):
        # create all 16 possible images
        self._trainingset = np.zeros([16,4])
        for i,im in enumerate(product([0,1],[0,1],[0,1],[0,1])):
            self._trainingset[i, :] = im

        # set the evaluation set to be the same as the training
        # usually, we would not do this!
        self._evaluationset = self._trainingset

    def training_set(self):
        while True:
            idx = np.random.randint(0,16)
            yield self._trainingset[idx, :]

    def evaluation_set(self):
        while True:
            idx = np.random.randint(0,16)
            yield self._evaluationset[idx, :]



if __name__ == '__main__':
    for i, im in enumerate(Dataloader().training_set()):
        print(im)
        if i>20:
            break

