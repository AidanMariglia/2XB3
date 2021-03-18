from lab8 import *
from min_heap import *
from random import shuffle, randint

def prim1(G):
    if G.number_of_nodes() == 0:
        return G
    edge_node = 0
    MST = WeightedGraph(G.number_of_nodes())
    A = [0]
    while(len(A) <= G.number_of_nodes()):
        min_edge = 1001
        for edge_info in G.adj[len(A) - 1]:
            if edge_info[1] < min_edge:
                min_edge = edge_info[1]
                edge_node = edge_info[0]
        if not MST.are_connected(len(A) - 1, edge_node):
            MST.add_edge(len(A) - 1, edge_node, min_edge)
        A.append(len(A))
    return MST

def prim2(G):
    if G.number_of_nodes() == 0:
        return G
    inf = 1001
    edges = MinHeap([Element(node, inf) for node in range(G.number_of_nodes())])
    mst = WeightedGraph(G.number_of_nodes())
    marked = [False for _ in range(G.number_of_nodes())]

    #for node in (G.adjacent_nodes(0)):
    #    edges.decrease_key(node[0], node[1])
    #marked[0] = True

    while not edges.is_empty():
        u = edges.extract_min()
        marked[u.value] = True
        flag = False
        for node in G.adjacent_nodes(u.value):
            if not marked[node[0]]:
                edges.decrease_key(node[0], node[1])
            
            elif u.key == node[1] and not flag:
                mst.add_edge(node[0], u.value, u.key)
                flag = True
                
    return mst

def primNathan(G):
    n = G.number_of_nodes()
    mst = WeightedGraph(n)
    INF = 1e9
    heap = MinHeap([Element(i, INF) for i in range(n)])

    visited = [False]*n

    for _ in range(n):
        u = heap.extract_min()
        visited[u.value] = True
        added = False

        for v, w in G.adjacent_nodes(u.value):
            if not visited[v]:
                heap.decrease_key(v,w)
            elif u.key == G.w(u.value, v) and not added:
                mst.add_edge(u.value, v, u.key)
                added = True
    return mst