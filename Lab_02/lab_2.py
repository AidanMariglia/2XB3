import timeit
import random

<<<<<<< HEAD

def copy():
    list1 = [1, 2, 3, 4, 5]
    list2 = list1.copy()
=======
def copy(Length):
    list1 = []
    for i in range(Length):
        list1.append(i)
    
>>>>>>> d1a1ac514fc1807a4df21bf4752e7dab7a30167d

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

def timetest(runs, Length):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        copy(Length)
        end = timeit.default_timer()
        total += end - start
    return total/runs

for i in range(100, 10000, 100):
    print(i, timetest(10, i))

