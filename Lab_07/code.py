from graphs import *
import random

def test_BFS2():
    test = Graph(7)

    test.add_edge(6,4)
    test.add_edge(4,3)
    test.add_edge(4,5)
    test.add_edge(5,2)
    test.add_edge(3,2)
    test.add_edge(5,1)
    test.add_edge(2,1)

    print(BFS2(test, 1, 6))

def test_BFS3():

    test = Graph(7)

    test.add_edge(1,2)
    test.add_edge(1,3)
    test.add_edge(2,4)
    test.add_edge(3,5)
    test.add_edge(3,4)
    test.add_edge(5,4)
    test.add_edge(4,6)

    print(BFS3(test, 1))

def test_DFS2():
    test = Graph(7)


    test.add_edge(6,4)
    test.add_edge(4,3)
    test.add_edge(4,5)
    test.add_edge(5,2)
    test.add_edge(3,2)
    test.add_edge(5,1)
    test.add_edge(2,1)

    print(DFS2(test, 1, 6))

def test_DFS3():
    test = Graph(7)

    for i in range(1,7):
        test.add_node()

    test.add_edge(1,2)
    test.add_edge(1,3)
    test.add_edge(2,4)
    test.add_edge(3,5)
    test.add_edge(3,4)
    test.add_edge(5,4)
    test.add_edge(4,6)

    print(DFS3(test, 1))

def test_is_connected():
    test = Graph(7)
    test.add_edge(6,4)
    
    print(is_connected(test))

def test_has_cycle():

    test = Graph(7)

    test.add_edge(0,1)
    test.add_edge(1,2)
    test.add_edge(1,3)
    test.add_edge(2,4)
    test.add_edge(3,5)
    test.add_edge(3,4)
    test.add_edge(5,4)
    test.add_edge(4,6)

    test2 = Graph(5)

    test2.add_edge(0,1)

    test2.add_edge(2,3)
    test2.add_edge(3,4)
    test2.add_edge(4,2)
    print(has_cycle(test2))

def create_random_graph(k, e):
    graph = Graph(k)
    count = e

    while count > 0:
        node1 = random.randint(0, k - 1)
        node2 = random.randint(0, k - 1)
        if graph.are_connected(node1, node2) or node1 == node2:
            pass
        else:
            graph.add_edge(node1, node2)
            count -= 1
    
    return graph

def portion_of_connected_graphs():
    count = 0
    for i in range(0, 500, 10):
        for j in range(100):
            new = create_random_graph(100, i)
            if is_connected(new):
                count += 1
        print(i, count/100)
        count = 0

def portion_of_graphs_with_cycle():
    count = 0
    for i in range(0, 100, 2):
        for j in range(100):
            new = create_random_graph(100, i)
            if has_cycle(new):
                count += 1
        print(i, count/100)
        count = 0

test_BFS2()
test_DFS2()
test_BFS3()
test_DFS3()