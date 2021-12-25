from collections import defaultdict

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

endpoints = []
for line in lines:
  halves = line.split()
  start = [int(p) for p in halves[0].split(',')]
  end = [int(p) for p in halves[2].split(',')]
  endpoints.append([start, end])

print(endpoints)
grid = defaultdict(int)
for start, end in endpoints:
  dx = end[0] - start[0]
  dy = end[1] - start[1]
  print(f'start, end: {start}, {end} (dx={dx}, dy={dy})')
  if dx != 0 and dy != 0:
    print('skipping...')
    continue
  if dx != 0:
    dx = dx // abs(dx)
  if dy != 0:
    dy = dy // abs(dy)

  p = start
  grid[tuple(p)] += 1
  while p != end:
    p[0] += dx
    p[1] += dy
    print(f'start, p, end: {start}, {p}, {end} (dx={dx}, dy={dy})')
    grid[tuple(p)] += 1

print(grid)

count = 0
for key, value in grid.items():
  if value >= 2:
    count += 1
    print(f'There are now {count} points at {key}')

print(f'count: {count}')
