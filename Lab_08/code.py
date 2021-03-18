from mst import *
from random import shuffle, randint
import timeit

def prim1Test():
    test = WeightedGraph(7)
    test.add_edge(0, 1, 1)
    test.add_edge(0, 2, 10)
    test.add_edge(0, 3, 2)
    test.add_edge(0, 5, 12)
    test.add_edge(1, 2, 3)
    test.add_edge(2, 3, 15)
    test.add_edge(2, 4, 18)
    test.add_edge(3, 4, 4)
    test.add_edge(3, 5, 5)
    test.add_edge(3, 6, 21)
    test.add_edge(4, 6, 6)
    test.add_edge(5, 6, 24)

    start = timeit.default_timer() 
    test2 = prim1(test)
    end = timeit.default_timer()
    total1 = end - start
    start = timeit.default_timer() 
    test1 = prim2(test)
    end = timeit.default_timer()
    total2 = end - start
    print(total1, total2)

    print(test2.number_of_nodes())
    print(test2.adjacent_nodes(0))
    print(test2.adjacent_nodes(1))
    print(test2.adjacent_nodes(2))
    print(test2.adjacent_nodes(3))
    print(test2.adjacent_nodes(4))
    print(test2.adjacent_nodes(5))
    print(test2.adjacent_nodes(6))

    print()

    print(test1.number_of_nodes())
    print(test1.adjacent_nodes(0))
    print(test1.adjacent_nodes(1))
    print(test1.adjacent_nodes(2))
    print(test1.adjacent_nodes(3))
    print(test1.adjacent_nodes(4))
    print(test1.adjacent_nodes(5))
    print(test1.adjacent_nodes(6))

def prim2Test():
    graph = WeightedGraph(4)
    graph.add_edge(0,1,1)
    graph.add_edge(1,3,2)
    graph.add_edge(3,2,5)
    graph.add_edge(2,0,4)
    graph.add_edge(0,3,3)

    mst = prim2(graph)

    for i in range(4):
        print(mst.adjacent_nodes(i))


def compare_test(nodes):
    for i in range(nodes, 100, 50):
        print(str(i) + "," + str(timetest(prim1, prim2, 1, nodes, i)))

def timetest(f1, f2, runs, nodes, edges):
    total1 = 0
    total2 = 0
    for _ in range(runs):
        rand_graph = generate_random_graph(nodes, edges)                                                 
        start = timeit.default_timer()                                          
        test2 = f1(rand_graph)
        print(test2.number_of_nodes())
        print(test2.adjacent_nodes(0))
        print(test2.adjacent_nodes(1))
        print(test2.adjacent_nodes(2))
        print(test2.adjacent_nodes(3))
        print(test2.adjacent_nodes(4))
        print(test2.adjacent_nodes(5))
        print(test2.adjacent_nodes(6))                                                               
        end = timeit.default_timer()
        total1 += end - start                                      
        start = timeit.default_timer()                                          
        test1 = f2(rand_graph) 
        print(test1.number_of_nodes())
        print(test1.adjacent_nodes(0))
        print(test1.adjacent_nodes(1))
        print(test1.adjacent_nodes(2))
        print(test1.adjacent_nodes(3))
        print(test1.adjacent_nodes(4))
        print(test1.adjacent_nodes(5))
        print(test1.adjacent_nodes(6))                                                               
        end = timeit.default_timer()                                          
        total2 += end - start                                                    
    return total1/runs, total2/runs

def generate_random_graph(nodes, edges):
    edgeWeights = [i for i in range(1,1001)]
    unVisitedNodes = [i for i in range(nodes)]
    shuffle(edgeWeights)
    shuffle(unVisitedNodes)
    randomGraph = WeightedGraph(nodes)

    currNode = unVisitedNodes.pop()
    while len(unVisitedNodes) > 0:
        nextNode = unVisitedNodes.pop()
        randomGraph.add_edge(currNode, nextNode, edgeWeights.pop())
        currNode = nextNode

    for i in range(edges - (nodes + 1)):

        node1 = randint(0, nodes - 1)
        node2 = randint(0, nodes - 1)

        while node1 == node2 or randomGraph.are_connected(node1, node2):
            node1 = randint(0, nodes - 1)
            node2 = randint(0, nodes - 1)

        randomGraph.add_edge(node1, node2, edgeWeights.pop())

    return randomGraph

compare_test(50)
