from lab10 import *

def check_degree(G, vertex):
    return len(G.adjacent_nodes(vertex))

def vc_approx2(G):
    degmap = {}
    cover = []
    for i in range(len(G.adj)):
        degmap[i] = check_degree(G, i)

    degmap = sorted(degmap.items(), key=lambda t : t[1] , reverse=True)

    for k, v in degmap:
        cover.append(k)
        if is_vertex_cover(G, cover):
            return cover

    return list(G.adj.keys())
    
def vc_approx1(G):
    nodes = list(G.adj.keys())
    C = []
    i = 0
    while(i < G.number_of_nodes()):
        randNum = random.randint(0, nodes.__len__() - 1)
        randNode = nodes[randNum]
        print(C)
        if randNode not in C:
            i += 1
            C.append(randNode)
        if is_vertex_cover(G, C):
            print("hello")
            return C
    return C


