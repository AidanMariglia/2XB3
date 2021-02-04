import random
import math
import timeit
from lab3 import *
from sorts import *

def worst_case_test():
    worst = []
    average = []
    runs = []

    for i in range(10, 1000, 10):
        runs.append(i)
        worst.append(worst_case_timetest(tri_pivot_quicksort, 20, i))
        average.append(timetest(tri_pivot_quicksort, 20, i))

    plt.plot(runs, average, label = "average")
    plt.plot(runs, worst, label = "worst case")
    plt.title("Worst Case vs Average Performance")
    plt.xlabel("Length")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

worst_case_test()