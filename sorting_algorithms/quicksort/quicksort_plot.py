import numpy as np
import matplotlib.pyplot as plt

class sort_class():
    def __init__(self, list, low, high):
        self.list = list
        self.low = low
        self.high = high
        self.count = 0

        self.sorted_list = self.sort()

    def sort(self):

        def plot(list, index, p):#, low, high):
            plt.figure()
            int = np.arange(0, len(list), 1)
            plt.bar(int, list)
            if p != 'ignore':
                for i in range(len(int)):
                    if int[i] == p:
                        plt.bar(p, list[i], color='r')
            #plt.vlines(low, list.min(), list.max(),color='k', ls='--')
            #plt.vlines(high, list.min(), list.max(),color='k', ls='--')
            plt.xlabel('Index', fontsize=12)
            plt.ylabel('Entry Value')
            plt.savefig('Plots/' + str(index) + '.png')
            plt.close()

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
                self.count += 1
                plot(list, self.count, p)#, low, high)
                quicksort(list, low, p - 1)
                quicksort(list, p + 1, high)
            sorted_list = list
            return sorted_list

        plot(self.list, self.count, 'ignore')#, self.low, self.high)
        sorted_list = quicksort(self.list, self.low, self.high)

        return sorted_list


unsorted_list = np.random.uniform(0, 100, 200)
print(unsorted_list)
sorted_list = sort_class(unsorted_list, 0, len(unsorted_list)-1).sorted_list
print(sorted_list)
