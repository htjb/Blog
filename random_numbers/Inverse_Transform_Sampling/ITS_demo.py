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

r_uniform, r_exp = [], []
for i in range(3):
    r_uniform.append(uniform(3).rand)
    r_exp.append(inverse_CDF(r_uniform[-1], lam))

F = CDF(x, lam)

color = ['k', 'r', 'purple']
plt.figure()
plt.plot(x, F)

for i in range(3):
    plt.plot(r_exp[i], r_uniform[i], ls='', marker='*',
        c=color[i], label='Set ' + str(i))

plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.savefig('ITS_demo.png')
plt.show()
