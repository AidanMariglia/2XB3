import timeit
import random

def copy(Length):
    list1 = []
    for i in range(Length):
        list1.append(i)
    

def lookups():
    
    for i in range(1000000):
        L[i] = random.randrange(500)

    x = 0

    for i in range(1000000):
        x = L[i]

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

