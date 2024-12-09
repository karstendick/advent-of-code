inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

# print(inp)

def find_guard(array):
  return [(i, j) 
          for i, row in enumerate(array) 
          for j, value in enumerate(row) 
          if value == '^'][0]

def in_bounds(r, c, num_rows, num_cols):
  return (0 <= r < num_rows) and (0 <= c < num_cols)

def turn_right(dr, dc):
  return (dc, -dr)

num_rows = len(inp)
num_cols = len(inp[0])
r, c = find_guard(inp)
dr, dc = -1, 0

visited = set()

while in_bounds(r, c, num_rows, num_cols):
  visited.add((r, c))
  nextr = r + dr
  nextc = c + dc
  if not in_bounds(nextr, nextc, num_rows, num_cols):
    break
  if inp[nextr][nextc] == '#':
    dr, dc = turn_right(dr, dc)
  else:
    r, c = nextr, nextc

print(len(visited))
