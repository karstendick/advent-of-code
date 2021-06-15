from collections import defaultdict

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

print(lines)

cells = defaultdict(int)

print(cells)

for y, line in enumerate(lines):
  for x, c in enumerate(line):
    cells[(x, y, 0)] = 1 if c == '#' else 0

print(cells)

def get_range(cells):
  xyzs = list(cells.keys())
  xs = [x for x,y,z in xyzs]
  ys = [y for x,y,z in xyzs]
  zs = [z for x,y,z in xyzs]

  return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)


def cells_string(cells):
  xmin, xmax, ymin, ymax, zmin, zmax = get_range(cells)

  s = ''
  for z in range(zmin, zmax+1):
    s += f'\nz={z}\n'
    for y in range(ymin, ymax+1):
      for x in range(xmin, xmax+1):
        s += '#' if cells[(x,y,z)] == 1 else '.'
      s += '\n'
  return s

print(cells_string(cells))

def count_num_neighbors(cells, x, y, z):
  n = 0
  for dz in range(-1, 2):
    for dy in range(-1, 2):
      for dx in range(-1, 2):
        if (dx, dy, dz) == (0,0,0):
          continue
        n += cells[(x+dx, y+dy, z+dz)]
  return n

def next_cycle(cells):
  new_cells = defaultdict(int)
  xmin, xmax, ymin, ymax, zmin, zmax = get_range(cells)
  for z in range(zmin-1, zmax+2):
    for y in range(ymin-1, ymax+2):
      for x in range(xmin-1, xmax+2):
        old_cell = cells[(x,y,z)]
        num_neighbors = count_num_neighbors(cells, x, y, z)
        if old_cell == 1:
          if num_neighbors in [2,3]:
            new_cells[(x,y,z)] = 1
          else:
            new_cells[(x,y,z)] = 0
        elif old_cell == 0:
          if num_neighbors == 3:
            new_cells[(x,y,z)] = 1
          else:
            new_cells[(x,y,z)] = 0
  return new_cells

cells1 = next_cycle(cells)
print(cells_string(cells1))

cells2 = next_cycle(cells1)
print(cells_string(cells2))

cells3 = next_cycle(cells2)
print(cells_string(cells3))

cells4 = next_cycle(cells3)
cells5 = next_cycle(cells4)
cells6 = next_cycle(cells5)

print(sum(cells6.values()))
