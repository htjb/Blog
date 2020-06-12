import numpy as np

class uniform():
    def __init__(self, size, low=0, high=1):
        self.rand = np.random.uniform(low, high, size)
