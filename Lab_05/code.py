import random
import timeit
from heap import *

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def create_sorted_list(n):
    L = create_random_list(n)
    L.sort()
    return L

def timetest(f, runs, Length):                                                  
    total = 0                                                                   
    list1 = []                                                                  
    for _ in range(runs):                                                       
        list1 = create_sorted_list(Length)                                      
        start = timeit.default_timer()                                          
        f(list1)                                                                
        end = timeit.default_timer()                                            
        total += end - start                                                    
    return total/runs 

<<<<<<< HEAD
for i in range(1000, 51000, 1000):
    print(str(i) + "," + str(timetest(Heap, 5, i)))
=======

#for i in range(100, 1100, 100):
    #print(str(i) + "," + str(timetest(Heap, 10, i)))

L = create_random_list(20)
new = Heap(L)
print(new.__str__())
>>>>>>> 45b59b949108ad759f2f18053bcb54b47218712c
