import numpy as np

from architecture import Block

class Dense(Block):
# ADD FUNCTION UPDATE CARLO 1
    """Fully connected layer: o = W i + b, with W of shape (m, n), b of shape (m,)."""
 
    def __init__(self, m, n, name=None, rng=None):
        super().__init__(name)

        rng = rng or np.random.default_rng()
        self.m, self.n = m, n
        # Scaled init keeps the induced local fields at a reasonable magnitude
        self.W = rng.normal(0.0, 1.0 / np.sqrt(n), size=(m, n))
        self.b = np.zeros(m)
        # CARLO THIS VARIABLE ARE USED TO STORED THE WEIGHT AND THE GRADIENT
        self.grad_W = np.zeros_like(self.W)
        self.grad_b = np.zeros_like(self.b)
 
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
 
        self.W_grad = g.T @ x             # dL/dW, shape (m, n)
        self.b_grad = g.sum(axis=0)       # dL/db, shape (m,)
 
        # Uses the weights from the forward pass: update() has not run yet
        self.backward_out = (g @ self.W).reshape(np.shape(self.forward_in))
        return self.backward_out
