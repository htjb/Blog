import numpy as np
import matplotlib.pyplot as plt
import time

class sort_class():
    def __init__(self, list, low, high):
        self.list = list
        self.low = low
        self.high = high

        self.sorted_list = self.sort()

    def sort(self):

        def partition(list, low, high):
            pivot = list[high]
            i = low
            for j in range(low, high):
                if list[j] < pivot:
                    list[i], list[j] = list[j], list[i]
                    i += 1
            list[i], list[high] = list[high], list[i]
            print(low, high)
            return i

        def quicksort(list, low, high):
            if low < high:
                p = partition(list, low, high)
                quicksort(list, low, p - 1)
                quicksort(list, p + 1, high)
            sorted_list = list
            return sorted_list

        sorted_list = quicksort(self.list, self.low, self.high)

        return sorted_list

# Selection sort....
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

#############################################

times_qs = []
for i in range(len(ndat)):
    unsorted_list = np.random.uniform(0, 100, int(ndat[i]))
    s = time.time()
    sorted_list = sort_class(unsorted_list, 0, len(unsorted_list)-1).sorted_list
    e = time.time()
    times_qs.append(e -s)

plt.figure()
plt.plot(ndat, times, label='Selection sort\nRecorded Times', c='r')
plt.plot(ndat, times_qs, label='Quicksort\nRecorded Times', c='k')
plt.plot(ndat, ndat**2/(ndat**2).max()*max(times), label=r'$\mathcal{O}(N^2)$', c='r', ls='--')
plt.plot(ndat, (ndat*np.log(ndat))/(ndat*np.log(ndat)).max()*max(times_qs), label=r'$\mathcal{O}(N\log(N))$', c='k', ls='--')
plt.xlabel(r'$N$', fontsize=12)
plt.ylabel('Times [s]', fontsize=12)
plt.legend()
plt.savefig('Times.png')
plt.show()
