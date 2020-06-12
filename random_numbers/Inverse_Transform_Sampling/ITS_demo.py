import numpy as np
import matplotlib.pyplot as plt
from uniform_dist import uniform

def prob(x, lam):
    return lam*np.exp(-lam*x)

def CDF(x, lam):
    return 1 - np.exp(-lam*x)

def inverse_CDF(y, lam):
    return -1/lam * np.log(1 - y)

x = np.linspace(0, 10, 100)
lam = 0.5


r_uniform = uniform(10).rand
r_exp = inverse_CDF(r_uniform, lam)

F = CDF(x, lam)

plt.figure()
plt.plot(x, F)
plt.plot(r_exp, r_uniform, ls='', marker='*')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.savefig('ITS_demo.png')
plt.show()
