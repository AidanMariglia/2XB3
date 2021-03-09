from graphs import *

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

test_BFS3()

def test_DFS2():
    test = Graph(6)


    test.add_edge(4,5)
    test.add_edge(5,2)
    test.add_edge(3,2)
    test.add_edge(5,1)
    test.add_edge(2,1)

    print(DFS2(test, 4, 2))

<<<<<<< HEAD
test_DFS2()

def test_DFS3():
    test = Graph(6)

    for i in range(1,7):
        test.add_node()

=======
def test_is_connected():
    test = Graph(7)
    
>>>>>>> 31cf42129385edf9eddff6d88bfd48e16b6b07cb
    test.add_edge(0,1)
    test.add_edge(1,2)
    test.add_edge(1,3)
    test.add_edge(2,4)
    test.add_edge(3,5)
    test.add_edge(3,4)
    test.add_edge(5,4)
<<<<<<< HEAD
    test.add_edge(4,6)

    print(DFS3(test, 1))

def test_is_connected():
    test = Graph(7)
=======
>>>>>>> 31cf42129385edf9eddff6d88bfd48e16b6b07cb
    test.add_edge(6,4)
    
    print(is_connected(test))

test_is_connected()

