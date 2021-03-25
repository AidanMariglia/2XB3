from shortest_paths import *
import timeit

def mystery_test(n, start, stop):
    for nodes in range(start, stop, 10):
        total = 0
        for _ in range(n):
            g = create_random_complete_graph(nodes, 1000)
            start = timeit.default_timer()
            mystery(g)
            total += timeit.default_timer() - start

        print(str(nodes) + "," + str(total/n))

def neg_mystery_test():
    G = DirectedWeightedGraph()
    G.add_node(0)
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)

    G.add_edge(0, 1, -1)
    G.add_edge(1, 2, -1)
    G.add_edge(2, 3, -1)
    G.add_edge(0, 3, -5)

    print(mystery(G))

#mystery_test(5, 10, 200)
neg_mystery_test()
