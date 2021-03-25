from lab9 import *

def all_pairs_dijkstra(G):
    matrix = [[999999 for _ in range(G.number_of_nodes())]\
                 for _ in range(G.number_of_nodes())]

    for source in range(G.number_of_nodes()):
        temp = dijkstra(G, source)
        for node in range(G.number_of_nodes()):
            matrix[source][node] = temp[node]

    return matrix


def all_pairs_bellman_ford(G):
    matrix = [[999999 for _ in range(G.number_of_nodes())]\
                 for _ in range(G.number_of_nodes())]

    for source in range(G.number_of_nodes()):
        temp = bellman_ford(G, source)
        for node in range(G.number_of_nodes()):
            matrix[node][source] = temp[node]

    return matrix
