from lab8 import *
from min_heap import *
from random import shuffle, randint

def prim1(WGraph):
    if WGraph.number_of_nodes() == 0:
        return WGraph
    edge_node = 0
    MST = WeightedGraph(WGraph.number_of_nodes())
    A = [0]
    while(len(A) <= WGraph.number_of_nodes()):
        min_edge = 1001
        for edge_info in WGraph.adj[len(A) - 1]:
            if edge_info[1] < min_edge:
                min_edge = edge_info[1]
                edge_node = edge_info[0]
        if not MST.are_connected(len(A) - 1, edge_node):
            MST.add_edge(len(A) - 1, edge_node, min_edge)
        A.append(len(A))
    return MST

def prim2(G):
    inf = 1001
    edges = MinHeap([Element(node, inf) for node in range(1,G.number_of_nodes())])
    mst = WeightedGraph(G.number_of_nodes())
    marked = [False for _ in range(G.number_of_nodes())]
    for node in (G.adjacent_nodes(0)):
        edges.decrease_key(node[0], node[1])
    marked[0] = True
    u = edges.extract_min()
    while not edges.is_empty():
        for node in G.adjacent_nodes(u.value):
            edges.decrease_key(node[0], node[1])
        u = edges.extract_min()
    return mst

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

test = generate_random_graph(50, 50)

prim2(test)