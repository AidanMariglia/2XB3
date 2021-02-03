import random
import math
import timeit
import matplotlib.pyplot as plt
from lab3 import *

def quicksort_inplace(a):
    sort_rec(a, 0, len(a) - 1)

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

def dual_pivot_quicksort(L):
    copy = dual_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def dual_pivot_quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot_left = min(L[0], L[1])
    pivot_right = max(L[0], L[1])
    left, right, mid = [], [], []

    for num in L[2:]:
        if (num < pivot_left):
            left.append(num)
        elif (num < pivot_right):
            mid.append(num)
        else:
            right.append(num)
    return dual_pivot_quicksort_copy(left) + [pivot_left] \
         + dual_pivot_quicksort_copy(mid) + [pivot_right] \
         + dual_pivot_quicksort_copy(right)


def tri_pivot_quicksort(L):
    copy = tri_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def tri_pivot_quicksort_copy(L):
    if len(L) < 2:
        return L

    if len(L) < 3:
        return [min(L[0], L[1]), max(L[0], L[1])]

    pivots = sorted([L[0], L[1], L[2]])
    pivot_left = pivots[0]
    pivot_mid = pivots[1]
    pivot_right = pivots[2]
    left, midleft, midright, right = [], [], [], []

    for num in L[3:]:
        if (num < pivot_left):
            left.append(num)
        elif (num < pivot_mid):
            midleft.append(num)
        elif (num < pivot_right):
            midright.append(num)
        else:
            right.append(num)

    return tri_pivot_quicksort_copy(left) + [pivot_left] \
        + tri_pivot_quicksort_copy(midleft) + [pivot_mid] \
        + tri_pivot_quicksort_copy(midright) + [pivot_right] \
        + tri_pivot_quicksort_copy(right)
        

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

def worst_case_timetest(f, runs, Length):
    total = 0
    list1 = []
    for _ in range(runs):
        list1 = random_reverse_list(Length)
        start = timeit.default_timer()
        f(list1)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def main():
    one = []
    two = []
    runs = []
    three = []

    for i in range(10, 1000, 10):
        runs.append(i)
        one.append(timetest(tri_pivot_quicksort, 20, i))
        two.append(worst_case_timetest(tri_pivot_quicksort, 20, i))

    plt.plot(runs, one, label = "average")
    plt.plot(runs, two, label = "worst case")
    plt.xlabel('Length')
    plt.ylabel('Runtime') 
    plt.title("Worst Case vs Average Peformance")
    plt.legend()
    plt.show()

def random_reverse_list(n):
    L = create_random_list(n)
    L.sort()
    i = 0
    for i in range(int(n/2)):
        L[i], L[n - 1 - i] = L[n - 1 - i], L[i]
    return L

list1 = random_reverse_list(3250)
tri_pivot_quicksort(list1)
print(list1)