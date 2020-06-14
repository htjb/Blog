import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 20, 1)
y = np.arange(-10, 20, 1)

X, Y = np.meshgrid(x, y)

Z = np.sqrt(X**2 + Y**2)

fig, ax = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 5))
cp = ax[0].contour(X, Y, Z)
ax[0].clabel(cp, inline=True, fontsize=10, fmt='%1.1f')

cp = ax[1].contourf(X, Y, Z, cmap='autumn')
plt.colorbar(cp, label='Radius')

fig.add_subplot(111, frame_on=False)
plt.tick_params(labelcolor="none", bottom=False, left=False)
plt.xlabel(r'$X$')
plt.ylabel(r'$Y$')
plt.subplots_adjust(wspace=0)
plt.savefig('Basic_example.png')
plt.show()
