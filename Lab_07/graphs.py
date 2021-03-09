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

def DFS2(G, node1, node2):
    path = []
    S = [node1]
    marked = {}
    
    for node in G.adj:
        marked[node] = False
    
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if marked[node] == False:
                    path.append(current_node)
                if node == node2:
                    path.append(node2)
                    return path
                S.append(node)
    return path



new = Graph(10)

new.add_edge(1, 2)

new.add_edge(2, 5)

new.add_edge(5, 8)

new.add_edge(8, 3)

print(DFS2(new, 1, 3))