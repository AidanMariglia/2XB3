from lab8 import *
from min_heap import *

def prim1(G):
    if G.number_of_nodes() == 0:
        return G
    edge_node = 0
    MST = WeightedGraph(G.number_of_nodes())
    A = [0]
    while(len(A) - 1 < G.number_of_nodes()):
        min_edge = 1001
        for i in A:
            for edge_info in G.adj[i]:
                if edge_info[1] < min_edge and not A.__contains__(edge_info[0]):
                    node1 = i
                    min_edge = edge_info[1]
                    edge_node = edge_info[0]
        if not MST.are_connected(node1, edge_node):
            MST.add_edge(node1, edge_node, min_edge)
        A.append(edge_node)
    return MST

def prim2(G):
    if G.number_of_nodes() == 0:
        return G
    inf = 1001
    edges = MinHeap([Element(node, inf) for node in range(G.number_of_nodes())])
    mst = WeightedGraph(G.number_of_nodes())
    marked = [False for _ in range(G.number_of_nodes())]

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
