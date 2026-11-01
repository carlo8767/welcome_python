from architecture import Block
from dataloader import Dataloader

## Task 5


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


if __name__ == '__main__':

    loader = Dataloader()

    l1 = ScaleBlock(scaling_factor=0.7)
    l2 = ScaleBlock(scaling_factor=0.5)
    l3 = OutputBlock(name='Output')
    for i, im in enumerate(loader.training_set()):
        print(im)
        x = l1.forward(im)
        x = l2.forward(x)
        x = l3.forward(x)

        if i > 5:
            break