import numpy as np
import matplotlib.pyplot as plt

def minimum(list):
    # Instead of np.min() just because we can.
    for i in range(len(list)):
        if i == 0:
            min = list[i]
        elif list[i] < min:
            min = list[i]

    return min

def plot(list, index):
    plt.figure()
    plt.bar(np.arange(0, len(list), 1), list)
    plt.xlabel('Index', fontsize=12)
    plt.ylabel('Entry Value')
    plt.savefig('Plots/' + str(index) + '.png')
    plt.close()


unsorted_list = list(np.random.uniform(0, 100, 100))
print(len(unsorted_list))
plot(unsorted_list, len(unsorted_list) + 1)

interim_list = unsorted_list
sorted_list = []
count = len(unsorted_list)
while len(interim_list) > 0:
    min = minimum(interim_list)
    sorted_list.append(min)
    interim_list.remove(min)
    plot(np.hstack([sorted_list, interim_list]), count)
    count -=1

print(sorted_list)
