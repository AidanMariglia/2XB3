from graphs import *

def test_BFS2():
    test = Graph(6)

    for i in range(1,7):
        test.add_node()

    test.add_edge(6,4)
    test.add_edge(4,3)
    test.add_edge(4,5)
    test.add_edge(5,2)
    test.add_edge(3,2)
    test.add_edge(5,1)
    test.add_edge(2,1)

    print(BFS2(test, 4, 2))

test_BFS2()

def test_DFS2():
    test = Graph(6)

    for i in range(1,7):
        test.add_node()

    test.add_edge(6,4)
    test.add_edge(4,3)
    test.add_edge(4,5)
    test.add_edge(5,2)
    test.add_edge(3,2)
    test.add_edge(5,1)
    test.add_edge(2,1)

    print(DFS2(test, 4, 2))

test_DFS2()

def test_DFS3():
    test = Graph(6)

    for i in range(1,7):
        test.add_node()

    test.add_edge(6,4)
    test.add_edge(4,3)
    test.add_edge(4,5)
    test.add_edge(5,2)
    test.add_edge(3,2)
    test.add_edge(5,1)
    test.add_edge(2,1)

    print(DFS3(test, 4))

test_DFS3()