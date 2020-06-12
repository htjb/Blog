import numpy as np
import matplotlib.pyplot as plt
from uniform_dist import uniform

x = np.linspace(0, 10, 100)
lam = [0.5, 1, 1.5, 2]

fig, axs = plt.subplots(2, 1, sharex=True)
for i in range(len(lam)):
    P = lam[i]*np.exp(-lam[i]*x)

    axs[0].plot(x, P, label=r'$\lambda$ = %2.1f' %lam[i])
    axs[0].set_ylabel(r'$P_d(x)$', fontsize=12)
    F = 1 - np.exp(-lam[i]*x)

    axs[1].plot(x, F)
    axs[1].set_ylabel(r'$F(X \leq x)$', fontsize=12)
    axs[1].set_xlabel(r'$x$', fontsize=12)
    axs[0].legend(fontsize=12)
plt.subplots_adjust(hspace=0)
plt.tight_layout()
plt.savefig('Probability_and_CDF.png')
plt.show()
