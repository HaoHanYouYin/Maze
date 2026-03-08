from maze.generator import *

def init_maze(width, height, generator):
    graph_width = width // 2
    graph_height = height // 2

    def point_to_int(x, y):
        return x * graph_width + y

    def int_to_point(pos):
        x = pos // graph_width
        y = pos % graph_width
        return x, y

    grid = [[1 for _ in range(width)] for _ in range(height)]

    graph = Graph(graph_width, graph_height)

    if generator == 'prim':
        graph = prim(graph_width, graph_height)
    elif generator == 'kruskal':
        graph = kruskal(graph_width, graph_height)
    elif generator == 'dfs':
        graph = dfs_generator(graph_width, graph_height)

    for index, neighborhood in enumerate(graph.points):
        x = int_to_point(index)[0]
        y = int_to_point(index)[1]
        grid[2 * x + 1][2 * y + 1] = 0
        for point in neighborhood:
            nx = int_to_point(point)[0]
            ny = int_to_point(point)[1]
            grid[nx + x + 1][ny + y + 1] = 0

    return grid