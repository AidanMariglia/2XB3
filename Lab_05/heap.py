import math
import random
import timeit

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap3()

    def build_heap1(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def build_heap2(self):
        aux = []
        for i in self.data: 
            aux.append(i)

        self.data = []
        self.length = 0

        for i in aux: 
            self.insert(i)

    def build_heap3(self):
        for i in range(self.length - 1):
            self.sink(i)
        if (not self.is_heap(0)):
            self.build_heap3()

    def is_heap(self, i):
        if (2 * i + 2 > self.length - 1):
            return True
        if(2 * i + 1 > self.length - 1 and self.data[i] < self.data[2 * i + 1]):
            return True
        if(self.data[i] > self.data[2 * i + 1] or self.data[i] > self.data[2 * i + 2]):
            return self.is_heap(2 * i + 1) and self.is_heap(2 * i + 2)
        else:
            return False

    def sink(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.sink(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

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

for i in range(10, 110, 10):
    print(i,timetest(Heap, 10, i))