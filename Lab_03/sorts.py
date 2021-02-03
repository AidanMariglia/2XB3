import random
import math
import timeit

def quicksort_inplace(a):
    pass

def sort_rec(a, lo, hi):
    pass

def partition(a, lo, hi):
    i = lo
    j = hi + 1
    pivot = a[lo]

    while(1):
        while (a[i + 1] < pivot):
            i += 1
            if (i == hi): break
        
        while (a[j - 1] > pivot):
            j -= 1
            if (j == lo): break
        
        if (i >= j): break
def exchange(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp