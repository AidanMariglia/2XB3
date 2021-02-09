from lab3 import *

def bubble_sort(L):
    j = 0
    for i in range(0, len(L)):
        for j in range(0, len(L) - i - 1):
            if(L[j] > L[j + 1]):
                exchange(L, j, j + 1)

    return L

def insertion_sort(L):
    j = 0
    for i in range(len(L)):
        j = i
        
        while(j > 0 and L[j] < L[j - 1]):
            exchange(L, j, j - 1)
            j -= 1

    return L

def selection_sort(L):
    j = 0
    for i in range(len(L)):
        min = i
        j = i
        while(j < len(L)):
            if (L[j] < L[min]):
                min = j
            j += 1
        exchange(L, i, min)
    return L



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
        return insertion_sort(L)

    pivots = insertion_sort([L[0], L[1], L[2]])
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


def quad_pivot_quicksort(L):
    copy = quad_pivot_quicksort_copy(L)

    for i in range(len(L)):
        L[i] = copy[i]

def quad_pivot_quicksort_copy(L):
    if len(L) < 2:
        return L
    if len(L) < 3:
        return insertion_sort(L)
    if len(L) < 4:
        return insertion_sort(L)

    pivots = insertion_sort(L[0:5])
    temps = [[],[],[],[],[]]
    for num in L[4:]:
        if (num < pivots[0]):
            temps[0].append(num)
        elif (num < pivots[1]):
            temps[1].append(num)
        elif (num < pivots[2]):
            temps[2].append(num)
        elif (num < pivots[3]):
            temps[3].append(num)
        else:
            temps[4].append(num)

    return quad_pivot_quicksort_copy(temps[0]) + [pivots[0]] \
        + quad_pivot_quicksort_copy(temps[1]) + [pivots[1]] \
        + quad_pivot_quicksort_copy(temps[2]) + [pivots[2]] \
        + quad_pivot_quicksort_copy(temps[3]) + [pivots[3]] \
        + quad_pivot_quicksort_copy(temps[4])

def random_reverse_list(n):
    L = create_random_list(n)
    L.sort()
    i = 0
    for i in range(int(n/2)):
        L[i], L[n - 1 - i] = L[n - 1 - i], L[i]
    return L

def final_sort(L):
    copy = final_sort_copy(L)

    for i in range(len(L)):
        L[i] = copy[i]

def final_sort_copy(L):
    if len(L) < 11:
        return insertion_sort(L)

    pivots = insertion_sort([L[0], L[1], L[2]])
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

