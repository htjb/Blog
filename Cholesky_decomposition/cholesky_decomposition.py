import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

x = np.linspace(40, 120, 100)

x_ = x/x.max()
N = 9

phi = np.empty([len(x), N])
for i in range(len(x)):
    for l in range(N):
        phi[i, l] = x_[i]**(l)

Q = phi.T @ phi

print(Q)

L = np.zeros(Q.shape)
for i in range(L.shape[0]):
    for j in range(L.shape[1]):
            if i == j:
                L[i, j] = np.sqrt(Q[i, j] -
                    np.sum([pow(L[j, k], 2) for k in range(j)]))
            elif i > j:
                L[i, j] = (1/L[j, j])*(Q[i, j] -
                    np.sum([L[i, k]*L[j, k] for k in range(j)]))

L_np = np.linalg.cholesky(Q)

A = np.linalg.inv(L)
A_np = np.linalg.inv(L_np)

Q_ = A @ Q @ A.T
Q_np = A_np @ Q @ A_np.T
plt.figure(figsize = (18, 5))
plt.subplot(1, 2, 1)
plt.imshow(Q_, cmap='jet')
cbar = plt.colorbar()
cbar.set_label(r'$Q\__{Cholesky: My Code}$')
plt.title('Cholesky: My Code')
plt.subplot(1, 2, 2)
plt.imshow(Q_np, cmap='jet')
cbar = plt.colorbar()
cbar.set_label(r'$Q\__{Cholesky: Numpy}$')
plt.title('Cholesky: Numpy')
#plt.savefig('Cholesky_Decomposition_x40-120.png')
plt.show()
