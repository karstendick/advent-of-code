from scipy.spatial import KDTree
import networkx as nx

points = []
with open("input.txt", "r") as f:
    for line in f:
        points.append(tuple(int(n) for n in line.strip().split(',')))

# print(points)
N = len(points)
K = N

tree = KDTree(points)


# Find closest pair
distances, indices = tree.query(points, k=K)  # k=2 because closest is itself
# print(f'distances: {distances}')
# print(f'indices: {indices}')

# A list of tuples of the form (distance, (point1, point2))
edges_by_distance = []
pairs = set()
for i in range(N):
    for j in range(1, K): # Skip k=1 (distance to self)
        dist = distances[i, j]
        idxs = indices[i, j]
        edge = tuple(sorted((points[i], points[idxs])))
        if edge in pairs:
            # Skip duplicate edges, i.e. (u, v) and (v, u)
            continue
        pairs.add(edge)
        edges_by_distance.append((dist, edge))

edges_by_distance.sort() # Sort by shortest distance
# print(edges_by_distance)


graph = nx.Graph()
i = 0
while True:
    n1, n2 = edges_by_distance[i][1]
    i += 1
    graph.add_edge(n1, n2)
    largest_circuit = max(nx.connected_components(graph), key=len)
    # print(f'largest_circuit: {largest_circuit}')
    if len(largest_circuit) == N:
        xprod = n1[0] * n2[0]
        # print((n1, n2))
        print(f'xprod: {xprod}')
        break
