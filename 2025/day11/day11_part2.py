from networkx import DiGraph
import networkx as nx
from collections import defaultdict

graph = DiGraph()

inp = []
# with open('example2.txt', 'r') as f:
with open("input.txt", "r") as f:
    for line in f:
        source, targets = line.strip().split(": ")
        targets = targets.split(" ")
        for target in targets:
            graph.add_edge(source, target)

# print(graph.nodes())
# print(graph.edges())

# There are 49516869367905070 paths from svr to out,
# so we can't enumerate all those paths


def count_paths(G: nx.DiGraph, source, target):
    """Count all paths from source to target in a DAG."""
    # Check if target is reachable from source
    if not nx.has_path(G, source, target):
        return 0

    # Get subgraph of nodes reachable from source that can reach target
    descendants = nx.descendants(G, source) | {source}
    ancestors = nx.ancestors(G, target) | {target}
    relevant = descendants & ancestors

    # Topological order on relevant subgraph
    subgraph = G.subgraph(relevant)
    topo_order = list(nx.topological_sort(subgraph))

    # DP: paths_to[node] = number of paths from source to node
    paths_to = {node: 0 for node in topo_order}
    paths_to[source] = 1

    for node in topo_order:
        for successor in subgraph.successors(node):
            paths_to[successor] += paths_to[node]

    return paths_to[target]


def count_paths_through_both(G: nx.DiGraph, start, end, n1, n2):
    """Count paths from start to end that pass through both n1 and n2."""
    # Case 1: start → n1 → n2 → end
    case1 = count_paths(G, start, n1) * count_paths(G, n1, n2) * count_paths(G, n2, end)

    # Case 2: start → n2 → n1 → end
    case2 = count_paths(G, start, n2) * count_paths(G, n2, n1) * count_paths(G, n1, end)

    return case1 + case2


print(count_paths_through_both(graph, "svr", "out", "dac", "fft"))
