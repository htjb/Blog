import numpy as np
import matplotlib.pyplot as plt
from uniform_dist import uniform

class normal():
    def __init__(self, mean, standard, size):

        x1 = uniform(size).rand
        x2 = uniform(size).rand

        R = np.sqrt(-2*np.log(x1))
        theta = 2*np.pi*x2

        r1 = R*np.sin(theta)*standard + mean
        #r2 = R*np.cos(theta)*standard + mean
        self.random = r1

random = normal(0, 5, 20000).random

mean = 0
standard = 5
x = np.linspace(-20, 20, 100)
gauss = (1/standard*np.sqrt(2*np.pi))* \
    np.exp(-1/2*((x-mean)/standard)**2)

gauss /=gauss.max()
gauss *= np.histogram(random, bins=500)[0].max()

plt.figure()
plt.hist(random, bins=500)
plt.plot(x, gauss)
plt.ylabel('Frequency')
plt.savefig('normal_random_numbers.png')
plt.show()
