from collections import defaultdict, deque

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append([int(x) for x in line.strip()])

# print(inp)

numrows = len(inp)
numcols = len(inp[0])

def in_bounds(rc):
  r, c = rc
  return (0 <= r < numrows) and (0 <= c < numcols)

def get_neighbors(r, c):
  neighbors = set()
  ds = [[-1, 0], [0, 1], [1, 0], [0, -1]] # NESW
  for (dr, dc) in ds:
    neighbors.add((r + dr, c + dc))
  return {n for n in neighbors if in_bounds(n)}


trailheads = set()
graph = defaultdict(set) # dict of (r,c) to set((r1,c1),...)
for r, row in enumerate(inp):
  for c, e in enumerate(row):
    node = (r, c)
    if e == 0:
      trailheads.add(node)
    neighbors = get_neighbors(r, c)
    for (nr, nc) in neighbors:
      if inp[nr][nc] == e + 1:
        graph[node].add((nr, nc))

# print(graph)
# print(trailheads)

from collections import deque

def bfs(graph, start):
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        queue.extend(neighbor for neighbor in graph[node])

    return traversal_order

def get_elev(rc):
  (r, c) = rc
  return inp[r][c]

total = 0
for trailhead in trailheads:
  trail = bfs(graph, trailhead)
  trail_rating = len([get_elev(rc) for rc in trail if get_elev(rc) == 9])
  total += trail_rating
print(total)
