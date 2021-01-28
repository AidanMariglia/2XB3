import timeit
import random
from openpyxl import Workbook

def copy(Length):
    list1 = []
    for i in range(Length):
        list1.append(i)
    

def lookups():
    L = []
    filename = "lookups.xlsx"
    workbook = Workbook()
    sheet = workbook.active


    for i in range(1000000):
        L.append(random.randrange(500))

    x = 0

    for i in range(1000000):
        start = timeit.default_timer()
        x = L[i]
        end = timeit.default_timer() - start
        #sheet["A"+str(i)] = i
        #sheet["B"+str(i)] = end

        #print(timeit.default_timer() - start)

    for i in range(100):
        sheet["A"+str(i+1)] = str(i)
        sheet["B"+str(i+1)] = str(i+1)

    workbook.save(filename=filename)




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


lookups()

