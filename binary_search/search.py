import numpy as np
from quicksort import sort

class binary_search():
    def __init__(self, x, T):
        self.x = x
        self.T = T
        self.index, self.bool = self.searching()

    def searching(self):
        L = 0
        H = len(self.x) - 1

        while L <= H:
            m = (L + H)//2
            if self.x[m] < self.T:
                L = m + 1
            elif self.x[m] > self.T:
                H = m - 1
            else: return m, True
        return None, False

T = 14
x = np.random.uniform(0, 100, 200)
x = np.append(x, T)
x = sort(x, 0, len(x)-1).sorted_list
search = binary_search(x, T)
print(search.index, x[search.index], search.bool)
