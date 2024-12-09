from collections import defaultdict
from itertools import combinations

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

# print(inp)
num_rows = len(inp)
num_cols = len(inp[0])

def in_bounds(r, c):
  return (0 <= r < num_rows) and (0 <= c < num_cols)

def get_antinodes(r1, c1, r2, c2):
  antinodes = set()
  dr = r2 - r1
  dc = c2 - c1

  r, c = r2, c2
  while in_bounds(r, c):
    antinodes.add((r,c))
    r, c = r + dr, c + dc

  r, c = r1, c1
  while in_bounds(r,c):
    antinodes.add((r,c))
    r, c = r - dr, c - dc

  return antinodes

# dict of antenna freq to locations
antennas = defaultdict(set)

for r, row in enumerate(inp):
  for c, e in enumerate(row):
    if e != '.':
      antennas[e].add((r, c))

# print(antennas)
antinodes = set()
for freq, locs in antennas.items():
  pairs = combinations(locs, 2)
  for pair in pairs:
    (r1, c1), (r2, c2) = pair
    antinodes |= get_antinodes(r1, c1, r2, c2)

# print(antinodes)
antinodes = {(r,c) for (r,c) in antinodes if in_bounds(r,c)}
# print(antinodes)
print(len(antinodes))
