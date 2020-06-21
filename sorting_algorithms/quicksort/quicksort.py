import numpy as np

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


unsorted_list = np.random.uniform(0, 10, 10)
print(unsorted_list)
sorted_list = sort_class(unsorted_list, 0, len(unsorted_list)-1).sorted_list
print(sorted_list)
