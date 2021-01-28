import timeit
import random

def lookups():
    
    for i in range(1000000):
        L[i] = random.randrange(500)

    x = 0

    for i in range(1000000):
        x = L[i]

    


   