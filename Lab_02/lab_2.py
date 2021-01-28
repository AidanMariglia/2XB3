import timeit
import random


def copy():
    list1 = [1, 2, 3, 4, 5]
    list2 = list1.copy()

def lookups():
    L = []

    for i in range(1000000):
        L.append(random.randrange(500))

    x = 0

    for i in range(1000000):
        start = timeit.default_timer()
        x = L[i]
        print(timeit.default_timer() - start)


lookups()

    


   
