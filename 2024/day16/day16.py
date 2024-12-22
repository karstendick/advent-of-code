from collections import defaultdict, deque
import heapq
import networkx as nx

inp = []
with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.strip())

# For input.txt:
start = (139, 1, 3)
end = (1, 139, 0)
# For example.txt:
# start = (13, 1, 1)
# end = (1, 13, 0)


print(start, end)

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def build_graph(start):
    graph = nx.DiGraph()
    for r, row in enumerate(inp):
        for c, e in enumerate(row):
            if e != "#":
                for z in range(4):
                    graph.add_node((r, c, z))

    for r, c, z in list(graph.nodes):
        dr, dc = directions[z]
        targetr, targetc = r + dr, c + dc
        if (targetr, targetc, z) in graph.nodes:
            graph.add_edge((r, c, z), (targetr, targetc, z), weight=1)
        for i in range(4):
            graph.add_edge((r, c, z), (r, c, i), weight=1000)

    return graph


graph = build_graph(start)
all_shortest_paths = nx.all_shortest_paths(graph, start, end, weight="weight")
seats = set()
for path in all_shortest_paths:
    for node in path:
        seats.add((node[0], node[1]))

print(len(seats))
