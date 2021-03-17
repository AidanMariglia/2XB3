from lab8 import *
from min_heap import *

def prim2(G):
    inf = 1001
    edges = MinHeap([Element(node, inf) for node in range(1,G.number_of_nodes())])
    mst = WeightedGraph(G.number_of_nodes())
    marked = [False for _ in range(G.number_of_nodes())]

    for node in (G.adjacent_nodes(0)):
        edges.decrease_key(node[0], node[1])
    marked[0] = True

    while not edges.is_empty():
        u = edges.extract_min()
        for node in G.adjacent_nodes(u.value):
            if u.key == node[1]:
                mst.add_edge(node[0], u.value, u.key)
                marked[u.value] = True
                print("marked " + str(u.value))

        for node in (G.adjacent_nodes(u.value)):
            if not marked[node[0]]:
                print("decreasing key " + str(node[0]))
                edges.decrease_key(node[0], node[1])

    return mst


    