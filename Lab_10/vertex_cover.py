from lab10 import *
import random

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


