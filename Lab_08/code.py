from mst import *

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


prim2Test()