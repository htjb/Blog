import numpy as np
import matplotlib.pyplot as plt
import time

def minimum(list):
    # Instead of np.min() just because we can.
    for i in range(len(list)):
        if i == 0:
            min = list[i]
        elif list[i] < min:
            min = list[i]

    return min

times = []
ndat = 10**np.arange(-3, 3, 0.1).astype(np.float)
for i in range(len(ndat)):
    unsorted_list = list(np.random.uniform(0, 100, int(ndat[i])))
    s = time.time()
    interim_list = unsorted_list
    sorted_list = []
    while len(interim_list) > 0:
        min = minimum(interim_list)
        sorted_list.append(min)
        interim_list.remove(min)
    e = time.time()
    times.append(e - s)

plt.figure()
plt.plot(ndat, times, label='Recorded Times')
plt.plot(ndat, ndat**2/(ndat**2).max()*max(times), label=r'$N^2$')
plt.xlabel(r'$N$', fontsize=12)
plt.ylabel('Times [s]', fontsize=12)
plt.legend()
plt.savefig('Times.png')
plt.show()
