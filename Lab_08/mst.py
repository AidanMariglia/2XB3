from lab8 import *

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
        print(edge_node)
        if not MST.are_connected(len(A) - 1, edge_node):
            MST.add_edge(len(A) - 1, edge_node, min_edge)
        A.append(len(A))
    print(A)
    return MST
    

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