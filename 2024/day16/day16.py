from collections import defaultdict, deque
import heapq

inp = []
with open("example_mod.txt", "r") as f:
    for line in f:
        inp.append(line.strip())

# print(inp)


def find_index_2d(array, value):
    for r, row in enumerate(array):
        if value in row:
            return (r, row.index(value))
    return None


start = find_index_2d(inp, "S")
end = find_index_2d(inp, "E")

print(start, end)


def rotate_cw(rc):
    r, c = rc
    return (c, -r)


def rotate_ccw(rc):
    r, c = rc
    return (-c, r)


def get_neighbor_dist_dir_tuples(node, dir):
    r, c = node
    if inp[r][c] == "E":  # Stop at end point
        return []
    neighbors = []
    dr, dc = dir
    cwdr, cwdc = rotate_cw(dir)
    ccwdr, ccwdc = rotate_ccw(dir)

    if inp[r + dr][c + dc] in ".E":  # Go straight
        neighbors.append(((r + dr, c + dc), 1, (dr, dc)))
    if inp[r + cwdr][c + cwdc] in ".E":  # Go right
        neighbors.append(((r + cwdr, c + cwdc), 1001, (cwdr, cwdc)))
    if inp[r + ccwdr][c + ccwdc] in ".E":  # Go left
        neighbors.append(((r + ccwdr, c + ccwdc), 1001, (ccwdr, ccwdc)))

    return neighbors


east = (0, 1)


def build_graph(start):
    graph = defaultdict(dict)  # {(0, 1): {(1, 1): 42, ...}, ...}
    visited = set()  # {(0, 0), (0, 1), ...}
    queue = deque([(start, east)])
    while queue:
        node, dir = queue.popleft()
        if node not in visited:
            visited.add(node)

            neighbor_dist_dir_tuples = get_neighbor_dist_dir_tuples(node, dir)
            unvisited_neighbor_dist_dir_tuples = [
                (n, ndist, ndir)
                for (n, ndist, ndir) in neighbor_dist_dir_tuples
                if n not in visited
            ]
            for n, ndist, ndir in unvisited_neighbor_dist_dir_tuples:
                graph[node][n] = ndist
                if n not in graph:
                    graph[n] = dict()
            unvisited_neighbor_dir_pairs = [
                (n, ndir) for (n, ndist, ndir) in unvisited_neighbor_dist_dir_tuples
            ]
            queue.extend(unvisited_neighbor_dir_pairs)
    graph[end] = {}
    return graph


def dijkstra(graph, start, target):
    # Priority queue to hold nodes and their distances
    pq = [(0, start)]  # (distance, node)
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        print(f"Visiting {current_node} with distance {current_distance}")
        print(f"Neighbors: {graph[current_node]}")

        # if current_distance > distances[current_node]:
        #     continue

        # if current_node == target:
        #     break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    print(f"distances: {distances}")
    return distances[target], path


graph = build_graph(start)
print(graph)

distance, path = dijkstra(graph, start, end)
print(
    f"Cheapest path from {start} to {end} is {path} with {len(path) - 1} steps with cost {distance}"
)
