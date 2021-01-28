import timeit
import random

def makelist(Length):
    list1 = []
    for i in range(Length):
        list1.append(i)
    return list1
    
def copy(List):
    List.copy()

def lookups():
    L = []

    for i in range(1000000):
        L.append(random.randrange(500))

    x = 0

    for i in range(1000000):
        start = timeit.default_timer()
        x = L[i]
        print(timeit.default_timer() - start)


def timetest(runs, Length):
    total = 0
    for _ in range(runs):
        list1 = makelist(Length)
        start = timeit.default_timer()
        copy(list1)
        end = timeit.default_timer()
        total += end - start
    return total/runs

for i in range(1000, 100000, 1000):
    print(i, timetest(10, i))

