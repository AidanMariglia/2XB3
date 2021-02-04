from sorts import *

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

def worst_case_timetest(f, runs, Length):
    total = 0
    list1 = []
    for _ in range(runs):
        list1 = random_reverse_list(Length)
        start = timeit.default_timer()
        f(list1)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def near_sorted_timetest(f, runs, Length, factor):
    total = 0
    list1 = []
    for _ in range(runs):
        list1 = create_near_sorted_list(Length, factor)
        start = timeit.default_timer()
        f(list1)
        end = timeit.default_timer()
        total += end - start
    return total/runs
    
def inplace_test():
    good = []
    bad = []
    runs = []

    for i in range(1000, 100000, 1000):
        runs.append(i)
        good.append(timetest(quicksort_inplace, 20, i))
        bad.append(timetest(my_quicksort, 20, i))

    plt.plot(runs, good, label = "good")
    plt.plot(runs, bad, label = "bad")
    plt.legend()
    plt.show()

def multi_pivot_test():
    single = []
    double = []
    triple = []
    quad = []
    runs = []
    three = []

    for i in range(10, 1000, 10):
        runs.append(i)
        single.append(timetest(my_quicksort, 20, i))
        double.append(timetest(dual_pivot_quicksort, 20, i))
        triple.append(timetest(tri_pivot_quicksort, 20, i))
        quad.append(timetest(tri_pivot_quicksort, 20, i))

    plt.plot(runs, single, label = "single pivot")
    plt.plot(runs, double, label = "double pivot")
    plt.plot(runs, triple, label = "triple pivot")
    plt.plot(runs, quad, label = "quad pivot")
    plt.legend()
    plt.show()

def worst_case_test():
    worst = []
    average = []
    runs = []

    for i in range(10, 1000, 10):
        runs.append(i)
        worst.append(worst_case_timetest(tri_pivot_quicksort, 20, i))
        average.append(timetest(tri_pivot_quicksort, 20, i))

    plt.plot(runs, average, label = "average")
    plt.plot(runs, worst, label = "worst case")
    plt.title("Worst Case vs Average Performance")
    plt.xlabel("Length")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

def near_sorted_list_test1():
    bubble = []
    selection = []
    insertion = []
    quick = []
    runs = []

    for i in range(2):
        runs.append(i)
        bubble.append(near_sorted_timetest(bubble_sort, 20, 1000, i))
        selection.append(near_sorted_timetest(selection_sort, 20, 1000, i))
        insertion.append(near_sorted_timetest(insertion_sort, 20, 1000, i))
        quick.append(near_sorted_timetest(tri_pivot_quicksort, 20, 1000, i))

    plt.plot(runs, bubble, label = "bubble")
    plt.plot(runs, selection, label = "selection")
    plt.plot(runs, insertion, label = "insertion")
    plt.plot(runs, quick, label = "quicksort")
    plt.title("Runtime of sorts vs sorted list")
    plt.xlabel("Factor of unsorted elements")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

def near_sorted_list_test2():
    bubble = []
    selection = []
    insertion = []
    quick = []
    runs = []

    for i in range(10):
        runs.append(i)
        bubble.append(near_sorted_timetest(bubble_sort, 20, 1000, i))
        selection.append(near_sorted_timetest(selection_sort, 20, 1000, i))
        insertion.append(near_sorted_timetest(insertion_sort, 20, 1000, i))
        quick.append(near_sorted_timetest(tri_pivot_quicksort, 20, 1000, i))

    plt.plot(runs, bubble, label = "bubble")
    plt.plot(runs, selection, label = "selection")
    plt.plot(runs, insertion, label = "insertion")
    plt.plot(runs, quick, label = "quicksort")
    plt.title("Runtime of sorts vs factor of unsorted elements")
    plt.xlabel("Factor of unsorted elements")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

def small_lists_test():
    bubble = []
    insert = []
    select = []
    quick = []
    members = []

    for i in range(1, 25):
        members.append(i)
        bubble.append(timetest(bubble_sort, 20, i))
        insert.append(timetest(insertion_sort, 20, i))
        select.append(timetest(selection_sort, 20, i))
        quick.append(timetest(tri_pivot_quicksort, 20, i))

    plt.plot(members, bubble, label = "bubble_sort")
    plt.plot(members, select, label = "selection_sort")
    plt.plot(members, insert, label = "insertion_sort")
    plt.plot(members, quick, label = "quick_sort")

    plt.plot.xlabel("size of list")
    plt.plot.ylabel("runtime")

    plt.legend()
    plt.show()

def final_test():
    quick, final, members = [], [], []

    for i in range(1000, 100000, 1000):
        quick.append(timetest(tri_pivot_quicksort, 20, i))
        final.append(timetest(final_sort, 20, i))
        members.append(i)

    plt.plot(members, quick, label = "Quick_Sort")
    plt.plot(members, final, label = "Final_Sort")
    
    plt.legend()
    plt.title("Tri pivot vs. final search")
    plt.xlabel("Size of List")
    plt.ylabel("Time")
    plt.show()