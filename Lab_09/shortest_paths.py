from lab9 import *

def bellman_ford_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())
    count = {}

    #Initialize distances
    for node in nodes:
        dist[node] = 99999
        count[node] = 0
    dist[source] = 0

    #Meat of the algorithm
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

graph = create_random_complete_graph(100, 1000)

current = dijkstra(graph, 0)

old = bellman_ford_approx(graph, 0, 99)

new = bellman_ford(graph, 0)

print(total_dist(current), total_dist(new), total_dist(old))