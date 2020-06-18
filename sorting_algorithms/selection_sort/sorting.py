import numpy as np

class sort_class():
    def __init__(self, unsorted_list):
        if type(list) is np.array:
            self.unsorted_list = list(unsorted_list)
        else:
            self.unsorted_list = unsorted_list

        self.sorted_list = self.sort()

    def sort(self):

        def minimum(list):
            # Instead of np.min() just because we can.
            for i in range(len(list)):
                if i == 0:
                    min = list[i]
                elif list[i] < min:
                    min = list[i]

            return min

        interim_list = self.unsorted_list
        sorted_list = []
        while len(interim_list) > 0:
            min = minimum(interim_list)
            sorted_list.append(min)
            interim_list.remove(min)

        return sorted_list


unsorted_list = [23, 54, 62, 1, 9, 45]
sorted_list = sort_class(unsorted_list).sorted_list
print(sorted_list)
