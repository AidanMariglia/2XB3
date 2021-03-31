from shortest_paths import *
import timeit

def bellman_ford_runtime_test(runs):
    rand_graph = create_random_complete_graph(100, 1000)
    for i in range(5, 105, 5):
        n = timetest(rand_graph, bellman_ford, bellman_ford_approx, runs, 50, i)
        print(str(i) + ',' + str(n[0]) + ',' + str(n[1]))

def bellman_ford_distance_test(runs):
    graphs = []
    for _ in range(runs):
        rand_graph = create_random_complete_graph(100, 1000)
        graphs.append(rand_graph)
    for i in range(5, 105, 5):
        n = distancetest(graphs, bellman_ford, bellman_ford_approx, runs, 50, i)
        print(str(i) + ',' + str(n[0]) + ',' + str(n[1]))

def timetest(graph, f1, f2, runs, source, k):
    total1 = 0
    total2 = 0
    for _ in range(runs):                                                 
        start = timeit.default_timer()                                          
        f1(graph, source)
        end = timeit.default_timer()                                                             
        total1 += end - start                                      
        start = timeit.default_timer()                                          
        f2(graph, source, k)
        end = timeit.default_timer()                                                                                                        
        total2 += end - start                                                  
    return total1/runs, total2/runs

def distancetest(graphs, f1, f2, runs, source, k):
    total1 = 0
    total2 = 0

    for graph in graphs:
        graph1 = f1(graph, source)
        graph2 = f2(graph, source, k)
        total1 += total_dist(graph1)
        total2 += total_dist(graph2)
    return total1, total2

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