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
    