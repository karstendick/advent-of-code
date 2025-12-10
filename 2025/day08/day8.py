from scipy.spatial import KDTree
import networkx as nx

points = []
with open("input.txt", "r") as f:
    for line in f:
        points.append(tuple(int(n) for n in line.strip().split(',')))

# print(points)
N = len(points)
K = 10

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

# closest_distance = distances[:, 1].min()  # Skip k=1 (distance to self)
# closest_idx = distances[:, 1].argmin()
# point1_idx = closest_idx
# point2_idx = indices[closest_idx, 1]

# print(f"Closest distance: {closest_distance}")
# print(f"Between points {point1_idx} and {point2_idx}")
# closest_pair = (points[point1_idx], points[point2_idx])
# print(closest_pair)

graph = nx.Graph()
for i in range(1000):
    n1, n2 = edges_by_distance[i][1]
    graph.add_edge(n1, n2)
# print()
# print(graph.edges())

circuit_sizes = [len(c) for c in sorted(nx.connected_components(graph), key=len, reverse=True)]
# print(circuit_sizes)

prod = 1
for i in range(3):
    prod *= circuit_sizes[i]
print(prod)
