import random
import math
import timeit
import matplotlib
from lab3 import *

def quicksort_inplace(a):
    start = timeit.default_timer()
    sort_rec(a, 0, len(a) - 1)
    end = timeit.default_timer() - start

def sort_rec(a, lo, hi):
    if (hi <= lo): return
    j = partition(a, lo, hi)
    sort_rec(a, lo, j-1)
    sort_rec(a, j+1, hi)

def partition(a, lo, hi):
    i = lo
    j = hi + 1
    pivot = a[lo]

    while(1):
        while (a[i + 1] < pivot):
            i += 1
            if (i == hi): break
        i += 1

        while (a[j - 1] > pivot):
            j -= 1
            if (j == lo): break
        j -= 1

        if (i >= j): break
        exchange(a, i, j)
        
    exchange(a, lo, j)
    return j

def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def main():

    a = create_random_list(100)
    quicksort_inplace(a)

    for i in a:
        print(i)

def timetest(runs, Length):
    total = 0
    list1 = []
    for _ in range(runs):
        list1 = create_random_list(Length)
        start = timeit.default_timer()
        quicksort_inplace(list1)
        end = timeit.default_timer()
        total += end - start
    return total/runs


for i in range(1000, 100000, 1000):
    print(i)
    print(timetest(50, i))
