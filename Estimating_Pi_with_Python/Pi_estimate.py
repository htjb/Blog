import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

y = np.sqrt(1 - x**2)

n = 10**np.arange(2, 8, 1)
pi_estimate = []
plt.figure(figsize=(12, 5))
for N in n:
    r_x = []
    r_y = []
    for i in range(N):
        r_x.append(np.random.uniform(0, 1))
        r_y.append(np.random.uniform(0, 1))

    counts_inside = 0
    counts_outside = 0
    for i in range(len(r_x)):
        distance = r_x[i]**2 + r_y[i]**2
        if distance <= 1:
            counts_inside += 1
        else:
            counts_outside +=1

    pi_estimate.append(4*(counts_inside/(counts_outside+counts_inside)))
    print(pi_estimate[-1])
    if np.any(N == [100, 10000]):
        if N == 100:
            plt.subplot(1, 2, 1)
        else:
            plt.subplot(1, 2, 2)
        plt.plot(r_x, r_y, ls='', marker='o')
        plt.plot(x, y)
        plt.title('N = %2d' %N)
plt.savefig('Pi_estimate_squares.png')
plt.show()
plt.close()

pi_estimate = np.array(pi_estimate)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(n, pi_estimate)
plt.hlines(np.pi, n.min(), n.max())
plt.xlabel('N', fontsize=12)
plt.ylabel(r'$\pi$', fontsize=12)
plt.xscale('log')
plt.subplot(1, 2, 2)
plt.plot(n, np.pi/pi_estimate)
plt.xlabel('N', fontsize=12)
plt.ylabel(r'$\pi_{numpy}/\pi$')
plt.xscale('log')
plt.savefig('Pi_estimate.png')
plt.show()
