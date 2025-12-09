import networkx as nx
from collections import defaultdict

grid = []
with open("input.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

# print(grid)

def print_grid(grid):
    for row in grid:
        print(''.join(row))

num_rows = len(grid)
num_cols = len(grid[0])

# print(f'num_rows: {num_rows}, num_cols: {num_cols}')

graph = nx.DiGraph()
start = None
path_counts = defaultdict(int)
for r in range(1, num_rows):
    for c in range(num_cols):
        if (grid[r - 1][c] == '|' or grid[r - 1][c] == 'S') and grid[r][c] == '.':
            if grid[r - 1][c] == 'S':
                start = (r, c)
                path_counts[(r, c)] = 1
            # Start the beam or keep it going down
            grid[r][c] = '|'
            graph.add_edge((r - 1, c), (r, c))
            path_counts[(r, c)] += path_counts[(r - 1, c)]
    for c in range(1, num_cols):
        if grid[r][c] == '^' and grid[r - 1][c] == '|':
            # split the beam
            grid[r][c - 1] = '|'
            grid[r][c + 1] = '|'
            graph.add_edge((r - 1, c), (r, c))
            graph.add_edge((r, c), (r, c - 1))
            graph.add_edge((r, c), (r, c + 1))
            path_counts[(r, c)] += path_counts[(r - 1, c)]
            path_counts[(r, c - 1)] += path_counts[(r, c)]
            path_counts[(r, c + 1)] += path_counts[(r, c)]
            

end = (num_rows, 0)
r = num_rows - 1
for c in range(num_cols):
    if grid[r][c] == '|':
        graph.add_edge((r, c), end)
        path_counts[end] += path_counts[(r, c)]

print(path_counts[end])

# N.B. This algorithm is too slow for the input.txt file:
# print(graph.edges)
# paths = nx.all_simple_paths(graph, start, end)
# num_paths = 0
# for path in paths:
#     num_paths += 1
# print(f'num_paths: {num_paths}')
