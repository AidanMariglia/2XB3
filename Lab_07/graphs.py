from lab7 import *

def BFS2(G, node1, node2):
    Q = deque([node1])
    path = []
    path.append(node1)
    marked = {node1 : True}

    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return path.append(node)
            if not marked[node]:
                Q.append(node)
                marked[node] = True

    return []

def DFS2():
    pass