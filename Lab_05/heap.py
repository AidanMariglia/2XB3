import math
import random
import timeit

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap2()

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
            if (2 * i + 1 > self.length - 1):
                return True
            if (self.data[i] >= self.data[2 * i + 1]):
                return True
            else:
                return False
        if(self.data[i] > self.data[2 * i + 1] and self.data[i] > self.data[2 * i + 2]):
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

L = [45, 76, 23, 12, 67, 89, 102, 7, 65, 67]

obj = Heap(L)

print(obj.__str__())
