from lab9 import *

def bellman_ford_approx(G, source, k):
    pred = {} 
    dist = {} 
    nodes = list(G.adj.keys())
    count = {}

    for node in nodes:
        dist[node] = 99999
        count[node] = 0
    dist[source] = 0

    for _ in range(G.number_of_nodes()):
        for node in nodes:
            if count[node] <= k:
                for neighbour in G.adj[node]:
                    if count[node] <= k:
                        if dist[neighbour] > dist[node] + G.w(node, neighbour):
                            dist[neighbour] = dist[node] + G.w(node, neighbour)
                            pred[neighbour] = node
                            count[node] += 1
                    else:
                        pass
            else:
                pass
    return dist


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
