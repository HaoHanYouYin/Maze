from scr.maze.generator import prim, kruskal, dfs_generator, Graph

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

    for id, next in enumerate(graph.points):
        x = int_to_point(id)[0]
        y = int_to_point(id)[1]
        grid[2 * x + 1][2 * y + 1] = 0
        for point in next:
            nx = int_to_point(point)[0]
            ny = int_to_point(point)[1]
            grid[nx + x + 1][ny + y + 1] = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    return grid