from lab8 import *
from min_heap import *

def prim2(G):

    if G.number_of_nodes() == 0:
        return G

    #as the greatest possible edge weight is 1000,
    #1001 will be used to represent infinity
    inf = 1001
    A = {0}
    mst = WeightedGraph(G.number_of_nodes())
    edges = MinHeap([Element(node, inf) for node in range(G.number_of_nodes())])


    for node in G.adjacent_nodes(0):
        edges.decrease_key(node[0], G.w(node[0], 0))
    
    prevMin = 0
    while not edges.is_empty():
        u = edges.extract_min()
        A.add(u.value)
        for node in G.adjacent_nodes(u.value):
            if u.key == node[1]:
                mst.add_edge(u.value, prevMin, G.w(u.value, prevMin))
            if node[0] not in A and \
                edges.get_element_from_value(node[0]).key > G.w(node[0], u.value):
                    edges.decrease_key(node[0], G.w(node[0], u.value))
        prevMin = u.value

    return mst

    