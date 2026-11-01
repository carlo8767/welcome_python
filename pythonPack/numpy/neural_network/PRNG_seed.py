import numpy as np

class PRNG:
    # Linear congruential generator
    def __init__(self, a=10, c=7, mod=10, seed=None):
        self.a=a
        self.c=c
        self.mod=mod
        self.xo = seed
        self.prev = (self.a * self.xo + self.c) % self.mod



if __name__  == '__main__':
    rg = np.random.default_rng()
    # DRAW FROM A RANDOM NUMBER
    # DEEP LEARNING
    values = rg.normal(0.0, 1.0 / np.sqrt(10), size=(10, 10))
    gen_np = np.zeros((1,1))
    # AT LEAST TWO DIMENSION
    s=np.atleast_2d(3.0)
    print(s)





