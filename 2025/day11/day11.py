from networkx import DiGraph
import networkx as nx
from collections import defaultdict

graph = DiGraph()

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    source, targets = line.strip().split(': ')
    targets = targets.split(' ')
    for target in targets:
      graph.add_edge(source, target)

# print(graph.nodes())
# print(graph.edges())

path_counts = defaultdict(int)
path_counts['you'] = 1
for node in nx.topological_sort(graph):
  if node == 'out':
    continue
  for neighbor in graph.neighbors(node):
    path_counts[neighbor] += path_counts[node]

print(path_counts['out'])
