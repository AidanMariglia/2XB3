from vertex_cover import *


def test_vc_approx_1(nodes, edges):
    print("approx_length, real_length")

    for i in range(10, edges, 10):
        g = create_random_graph(nodes, i)
        print(len(vc_approx1(g)), end=',')
        print(len(vertex_cover(g)))


test_vc_approx_1(20, 190)