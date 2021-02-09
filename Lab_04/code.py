from sorts import *
from lab4 import *
import matplotlib.pyplot as plt
import timeit

def near_sorted_timetest(f, runs, Length, factor):
    total = 0
    list1 = []
    for _ in range(runs):
        list1 = create_near_sorted_list(Length, factor)
        start = timeit.default_timer()
        f(list1)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def near_sorted_list_test():
    merge = []
    runs = []
    factor = 0
    for i in range(6):
        runs.append(factor)
        merge.append(near_sorted_timetest(mergesort, 50, 10000, factor))
        factor += 0.1
    plt.plot(runs, merge, label = "mergesort")
    plt.title("Runtime of mergesort vs factor of unsorted elements")
    plt.xlabel("Factor of unsorted elements")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

near_sorted_list_test()