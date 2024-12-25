import networkx as nx

inp = []
with open("input.txt", "r") as f:
    for line in f:
        c, r = tuple(int(n) for n in line.split(','))
        inp.append((r, c))

# numrows, numcols, numbytes = 7, 7, 12 # example
numrows, numcols, numbytes = 71, 71, 1024 # input
targetr, targetc = numrows - 1, numcols - 1
starting_nodes = set(inp[:numbytes])
# print(inp)

drs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # NESW

graph = nx.Graph()
for r in range(numrows):
    for c in range(numcols):
        if (r, c) in starting_nodes:
            continue # skip corrupted locations
        graph.add_node((r, c))

for r, c in list(graph.nodes):
    for dr, dc in drs:
        nr, nc = r + dr, c + dc
        if (nr, nc) in graph.nodes:
            graph.add_edge((r, c), (nr, nc))

i = numbytes
while i < len(inp):
    nextr, nextc = inp[i]
    graph.remove_node((nextr, nextc))
    try:
        nx.shortest_path_length(graph, (0, 0), (targetr, targetc))
    except nx.NetworkXNoPath:
        print(f'{nextc},{nextr}')
        break
    i += 1
