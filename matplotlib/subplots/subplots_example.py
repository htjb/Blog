import matplotlib.pyplot as plt

plt.subplot(211)
plt.subplot(212)
plt.savefig('Fig1.png')
#plt.show()
plt.close()

import numpy as np
x = np.linspace(3, 5, 100)
y = x**2

x1 = np.linspace(2, 5, 100)
y1 = x**3

nrows, ncols = 2, 1
fig, axs = plt.subplots(nrows, ncols, sharex='col')
axs[0].plot(x, y)
axs[1].plot(x1, y1)
plt.savefig('Fig2.png')
#plt.show()
plt.close()

nrows, ncols = 2, 1
fig, axs = plt.subplots(nrows, ncols, sharex='col')
axs[0].plot(x, y)
axs[1].plot(x1, y1)
fig.add_subplot(111, frame_on=False)
plt.tick_params(labelcolor="none", bottom=False, left=False)
plt.xlabel('x')
plt.ylabel('y')
plt.subplots_adjust(hspace=0)
plt.savefig('Fig3.png')
#plt.show()
plt.close()

nrows, ncols = 4, 4
fig, axs = plt.subplots(nrows, ncols, figsize=(10, 10), sharey=True, sharex=True)
for i in range(ncols):
    for j in range(nrows):
        if j == 3:
            axs[j, i].tick_params(axis='x', labelrotation=90)
        if i > j:
            axs[j, i].axis('off')

fig.add_subplot(111, frame_on=False)
plt.tick_params(labelcolor="none", bottom=False, left=False)
plt.xlabel('x', fontsize=12, labelpad=20)
plt.ylabel('y', fontsize=12)
plt.tight_layout()
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('Fig4.png')
plt.show()
plt.close()
