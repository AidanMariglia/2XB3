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

    print(BFS2(test, 1, 6))

test_BFS2()