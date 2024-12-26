from collections import Counter
import networkx as nx

inp = []
with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.strip())

# print(inp)

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


def manhattan_dist(node1, node2):
    r1, c1 = node1
    r2, c2 = node2
    return abs(r1 - r2) + abs(c1 - c2)


# cheat_threshold = 50  # for example
cheat_threshold = 100

dist_from_start = dict(nx.single_source_all_shortest_paths(graph, source=start))
total = 0
for k1, v1 in dist_from_start.items():
    for k2, v2 in dist_from_start.items():
        d = manhattan_dist(k1, k2)
        l1 = len(v1[0])
        l2 = len(v2[0])
        if d <= 20 and l2 - l1 - d >= cheat_threshold:
            total += 1
print(total)
