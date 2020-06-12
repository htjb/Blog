import numpy as np
import matplotlib.pyplot as plt
from uniform_dist import uniform

class exponential():
    def __init__(self, lam, size):
        y = uniform(size).rand
        self.random = -1/lam * np.log(1 - y)

random = exponential(0.5, 20000).random
random2 = exponential(1, 3000).random

plt.figure()
plt.hist(random, bins=500, label=r'$\lambda$ = 0.5')
plt.hist(random2, bins=50, label=r'$\lambda$ = 1')
plt.legend(fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xlabel('x', fontsize=12)
plt.savefig('exponential_random_numbers.png')
plt.show()
