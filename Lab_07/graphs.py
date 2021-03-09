from lab7 import *

def BFS2(G, node1, node2):
    Q = deque([node1])
    path = {node1 : [node1]}
    marked = {node1 : True}

    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return path[current_node] + [node]
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                path[node] = path[current_node] + [node]

    return []

def DFS2(G, node1, node2):
    path = {node1 : [node1]}
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
                    path[node] = path[current_node] + [node]
                if node == node2:
                    return path[current_node] + [node]
                S.append(node)
    return []

def DFS3(G, node1):
    path = {}
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
                    print(current_node)
                    path[node] = current_node
                S.append(node)
    return path