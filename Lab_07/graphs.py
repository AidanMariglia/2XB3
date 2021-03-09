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
    return path

def BFS3(G, start):
    Q = deque([start])
    marked = {start : True}
    pred = {}
    for node in G.adj:
        if node != start:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True

                if node not in pred:
                    pred[node] = current_node

    return pred


def is_connected(G):
    if G.number_of_nodes() == 0: return False

    connections = BFS3(G, 1) 
    
    if len(connections) + 1 != G.number_of_nodes():
        return False
    else:
        return True




