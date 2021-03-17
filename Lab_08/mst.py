from lab8 import *
from min_heap import *

def prim2(G):

    if G.number_of_nodes() == 0:
        return G

    #as the greatest possible edge weight is 1000,
    #1001 will be used to represent infinity
    inf = 1001
    A = [0]
    mst = WeightedGraph(G.number_of_nodes())
    edges = MinHeap([Element(node, inf) for node in range(G.number_of_nodes())])


    for node in G.adjacent_nodes(0):
        edges.decrease_key(node, G.w(node, 0))

    while edges.length != 0:
        u = edges.extract_min()
        mst.add_edge()
        for v in G.adjacent_nodes(u.value):
            edges.decrease_key(v, G.w(v, u.value))

    