import random
import timeit
from heap import *

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

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

for i in range(1000, 51000, 1000):
    print(str(i) + "," + str(timetest(Heap, 5, i)))