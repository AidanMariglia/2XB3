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

def near_sorted_list_test1():
    merge = []
    runs = []
    factor = 0
    for i in range(6):
        runs.append(factor)
        merge.append(near_sorted_timetest(mergesort, 20, 100000, factor))
        factor += 0.1
    plt.plot(runs, merge, label = "mergesort")
    plt.title("Runtime of mergesort vs factor of unsorted elements")
    plt.xlabel("Factor of unsorted elements")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

def timetest(f, runs, Length):                                                  
    total = 0                                                                   
    list1 = []                                                                  
    for _ in range(runs):                                                       
        list1 = create_random_list(Length)                                      
        start = timeit.default_timer()                                          
        f(list1)                                                                
        end = timeit.default_timer()                                            
        total += end - start                                                    
    return total/runs 

def bottom_up_test():
    timebottom = []
    timemerge = []
    length = []

    for i in range(1000, 100000, 1000):
        length.append(i)
        timebottom.append(timetest(mergesort_bottom, 20, i))
        timemerge.append(timetest(mergesort, 20, i))

    plt.plot(length, timebottom, label = "Bottom up Merge")
    plt.plot(length, timemerge, label = "Top down Merge")
    plt.title("Average runtime of Bottom up merge vs. Top down merge at progressive list lengths")
    ply.xlabel("Length of test list")
    plt.ylabel("Running time (s)")
    plt.legend()
    plt.show()

def merge_three_test():
    timethree = []
    timemerge = []
    length = []

    for i in range(1000, 100000, 1000):
        length.append(i)
        timebottom.append(timetest(mergesort_three, 20, i))
        timemerge.append(timetest(mergesort, 20, i))

    plt.plot(length, timethree, label = "Three-way Merge")
    plt.plot(length, timemerge, label = "Two-way Merge")
    plt.title("Average runtime of Two way vs Three way mergesort at progressive list lengths")
    ply.xlabel("Length of test list")
    plt.ylabel("Running time (s)")
    plt.legend()
    plt.show()

#near_sorted_list_test1()
#bottom_up_test()

a = create_random_list(10)
mergesort_three(a)
print(a)