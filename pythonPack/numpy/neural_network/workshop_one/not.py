from architecture import Block
from dataloader import Dataloader


## TASK 4

class NOTBlock(Block):

    def forward(self, input):
        super().forward(input)
        self.forward_out = 1. - input
        return self.forward_out


class OutputBlock(Block):

    def forward(self, input):
        super().forward(input)
        print(input)
        return input


if __name__ == '__main__':

    loader = Dataloader()

    l1 = NOTBlock(name='NotBlock')
    l2 = OutputBlock(name='Output')

    for i, im in enumerate(loader.training_set()):
        x = l1.forward(im)
        x = l2.forward(x)

        if i > 5:
            break

