import numpy as np
from quicksort import sort
import matplotlib.pyplot as plt

class binary_search():
    def __init__(self, x, T):
        self.x = x
        self.T = T
        self.index, self.bool = self.searching()

    def searching(self):

        L = 0
        H = len(self.x) - 1

        j = np.arange(0, len(self.x), 1)

        count = 0
        while L <= H:
            m = (L + H)//2

            plt.figure()
            for i in range(len(j)):
                if j[i] == L:
                    plt.bar(L, self.x[L], color='orange', label='L, H')
                elif j[i] == H:
                    plt.bar(H, self.x[H], color='orange')
                elif j[i] == m:
                    plt.bar(m, self.x[m], color='r', label='m')
                elif j[i] > H or j[i] < L:
                    plt.bar(j[i], self.x[i], color='b', alpha=0.5)
                else:
                    plt.bar(j[i], self.x[i], color='b')
            plt.xlabel('Index', fontsize=12)
            plt.ylabel('Entry Value', fontsize=12)
            plt.legend(loc=2)
            plt.tight_layout()
            plt.savefig('Plots/' + str(count) +'.png')
            #plt.show()
            plt.close()

            if self.x[m] < self.T:
                L = m + 1
            elif self.x[m] > self.T:
                H = m - 1
            else: return m, True
            count += 1
        return None, False

T = 16
x = np.random.uniform(0, 100, 100)
x = np.append(x, T)
x = sort(x, 0, len(x)-1).sorted_list
search = binary_search(x, T)
