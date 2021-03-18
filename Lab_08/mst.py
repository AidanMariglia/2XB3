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
        if not marked[node[0]]:
            edges.decrease_key(node[0], node[1])

        #for node in (G.adjacent_nodes(u.value)):
        #    if not marked[node[0]]:
        #        edges.decrease_key(node[0], node[1])

    return mst

def prim2_2(G):
    inf = 1001
    edges = MinHeap([Element(node, inf) for node in range(1,G.number_of_nodes())])
    mst = WeightedGraph(G.number_of_nodes())
    marked = [False for _ in range(G.number_of_nodes())]

    for node in (G.adjacent_nodes(0)):
        edges.decrease_key(node[0], node[1])
    
    prevMin = Element(0, inf)
    marked[0] = True

    while not edges.is_empty():
        u = edges.extract_min()
        for node in G.adjacent_nodes(prevMin.value):
            if not marked[node[0]]:
                edges.decrease_key(node[0], node[1])
        
        newMin = edges.extract_min()
        mst.add_edge(prevMin.value, newMin.value, newMin.key)
        prevMin = newMin

            

    return mst
