import random

class Graph:
    def __init__(self, graph_width, graph_height):
        self.graph_width = graph_width
        self.graph_height = graph_height
        # points[编号] = [编号合集]
        self.points = [[] for _ in range(graph_width * graph_height)]


def prim(g_width, g_height) -> Graph:
    pass

def kruskal(graph_width, graph_height) -> Graph:
    # 定义并查集函数
    def find(x):
        if p[x] == x:
            return x
        else:
            p[x] = find(p[x])
            return p[x]

    def merge(a, b):
        pa = find(a)
        pb = find(b)
        if pa != pb:
            p[pa] = pb

    def point_to_int(x, y):
        return x * graph_width + y

    # 定义并查集和图
    p = [i for i in range(graph_width * graph_height)]
    g = Graph(graph_width, graph_height)
    edges = []

    for i in range(graph_height):
        for j in range(graph_width):
            if j + 1 < graph_width:
                edges.append((point_to_int(i, j), point_to_int(i, j + 1)))
            if i + 1 < graph_height:
                edges.append((point_to_int(i, j), point_to_int(i + 1, j)))

    while edges:
        rand_edge_id = random.randint(0, len(edges) - 1)
        cur_edge = edges[rand_edge_id]
        edges[rand_edge_id] = edges[-1]
        edges.pop()
        if find(cur_edge[0]) != find(cur_edge[1]):
            merge(cur_edge[0], cur_edge[1])
            g.points[cur_edge[0]].append(cur_edge[1])
    return g

def dfs_generator(graph_width, graph_height) -> Graph:
    pass
