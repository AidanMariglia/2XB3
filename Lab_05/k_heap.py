import math
import random

class k_heap:

    def __init__(self, values, k):
        self.data = values
        self.length = len(values)
        self.k = k
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // self.k - 1, -1, -1 ):
            self.sink(i)

    def parent(self, i):
        return (i + self.k - 1) // self.k - 1

    def children(self, i):
        return [self.k * i + j for j in range(1, self.k + 1)]

    def sink(self, i):
        largest_known = i

        if self.k * i + 1 < self.length and \
                self.data[self.k * i + 1] > self.data[i]:
                    largest_known = self.k * i + 1

        for j in range(2, self.k + 1):
            if self.k * i + j < self.length and \
                self.data[self.k * i + j] > self.data[largest_known]:
                    largest_known = self.k * i + j

        if largest_known != i:
            self.data[i], self.data[largest_known] =\
                self.data[largest_known], self.data[i]
            self.sink(largest_known)

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

L = create_random_list(10)

print(L)

obj = k_heap(L, 2)

print(obj.__str__())