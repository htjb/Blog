import numpy as np

class ldl(object):
    #ldl decomposition
    def __init__(self, Q):
        self.Q = Q
        self.L, self.D = self.calc()

    def calc(self):
        L = np.zeros(self.Q.shape)
        D = np.zeros(len(self.Q))
        for i in range(L.shape[1]):
            for j in range(L.shape[0]):
                D[j] = (self.Q[j, j] - np.sum([L[j, k]**2*D[k]
                        for k in range(j)]))
                if i == j:
                    L[i, j] = 1
                if i > j:
                    L[i, j] = ((1/D[j])*(self.Q[i, j] -
                        np.sum([L[i, k]*L[j, k]*D[k] for k in range(j)])))
        D = D * np.identity(len(self.Q))
        return L, D

x = np.linspace(40, 120, 100)
x_ = x/x.max()
N = 6

phi = np.empty([len(x), N])
for i in range(len(x)):
    for l in range(N):
        phi[i, l] = x_[i]**(l)

Q = phi.T @ phi

LD = ldl(Q)
L, D = LD.L, LD.D
print(Q - L @ D @ L.T)

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(L, cmap='jet')
cbar = plt.colorbar()
cbar.set_label(r'$L$')

plt.subplot(1, 3, 2)
plt.imshow(D, cmap='jet')
cbar = plt.colorbar()
cbar.set_label(r'$D$')

plt.subplot(1, 3, 3)
plt.imshow(L.T, cmap='jet')
cbar = plt.colorbar()
cbar.set_label(r'$L^T$')
plt.subplots_adjust(wspace=0.3)
plt.suptitle('LDL Decomposition')
plt.savefig('LDL_Decomposition.png')
plt.show()
