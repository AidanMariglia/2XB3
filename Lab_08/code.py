from mst import *
from random import shuffle, randint

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

    test2 = prim1(test)

    print(test2.number_of_nodes())
    print(test2.adjacent_nodes(0))
    print(test2.adjacent_nodes(1))
    print(test2.adjacent_nodes(2))
    print(test2.adjacent_nodes(3))
    print(test2.adjacent_nodes(4))
    print(test2.adjacent_nodes(5))
    print(test2.adjacent_nodes(6))

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


def compare_test():
    pass

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