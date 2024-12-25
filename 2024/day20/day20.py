from collections import Counter
import networkx as nx

inp = []
with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.strip())

# print(inp)
numrows = len(inp)
numcols = len(inp[0])

drs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW
graph = nx.Graph()
for r, row in enumerate(inp):
    for c, e in enumerate(row):
        if e in ".SE":
            graph.add_node((r, c))
        if e == "S":
            start = (r, c)
        elif e == "E":
            end = (r, c)

for r, c in list(graph.nodes):
    for dr, dc in drs:
        nr, nc = r + dr, c + dc
        if (nr, nc) in graph.nodes:
            graph.add_edge((r, c), (nr, nc))

shortest_path = nx.shortest_path(graph, start, end)
# print(shortest_path)
# print(len(shortest_path))
shortest_path_length = nx.shortest_path_length(graph, start, end)
# print(shortest_path_length)

cheat_counts = Counter()
for r in range(1, numrows):
    for c in range(1, numcols):
        e = inp[r][c]
        if e != '#':
            continue
        shortcut_graph = graph.copy()
        shortcut_graph.add_node((r, c))
        num_edges_added = 0
        for dr, dc in drs:
            nr, nc = r + dr, c + dc
            if (nr, nc) in graph.nodes:
                shortcut_graph.add_edge((r, c), (nr, nc))
                num_edges_added += 1
        if num_edges_added == 0:
            continue
        print(f'Adding ({r}, {c}) ...')
        this_path_length = nx.shortest_path_length(shortcut_graph, start, end)
        cheat_counts[shortest_path_length - this_path_length] += 1

# print(cheat_counts)
total = 0
for ps, num_cheats in cheat_counts.items():
    # print(f'There are {num_cheats} that save {ps} picoseconds.')
    if ps >= 100:
        total += num_cheats
print(total)
