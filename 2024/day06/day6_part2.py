from copy import deepcopy

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(list(line.strip()))

# print(inp)
num_rows = len(inp)
num_cols = len(inp[0])

def find_guard(array):
  return [(i, j) 
          for i, row in enumerate(array) 
          for j, value in enumerate(row) 
          if value == '^'][0]

def in_bounds(r, c, num_rows, num_cols):
  return (0 <= r < num_rows) and (0 <= c < num_cols)

def turn_right(dr, dc):
  return (dc, -dr)

def one_step(r, c, dr, dc, array):
  while in_bounds(r, c, num_rows, num_cols):
    nextr = r + dr
    nextc = c + dc
    if not in_bounds(nextr, nextc, num_rows, num_cols):
      return (-1, -1), (-99, -99), False
    if array[nextr][nextc] == '#':
      dr, dc = turn_right(dr, dc)
    else:
      r, c = nextr, nextc
      return (r, c), (dr, dc), True
  return (-1, -1), (-99, -99), False

# Floyd's cycle-finding algorithm
def detect_loop(array):
  slowr, slowc = find_guard(array)
  slowdr, slowdc = -1, 0
  fastr, fastc = slowr, slowc
  fastdr, fastdc = slowdr, slowdc

  in_bounds = True
  while in_bounds:
    (slowr, slowc), (slowdr, slowdc), slow_in_bounds = one_step(slowr, slowc, slowdr, slowdc, array)
    if not slow_in_bounds:
      return False
    (fastr, fastc), (fastdr, fastdc), fast_in_bounds = one_step(fastr, fastc, fastdr, fastdc, array)
    if not fast_in_bounds:
      return False
    (fastr, fastc), (fastdr, fastdc), fast_in_bounds = one_step(fastr, fastc, fastdr, fastdc, array)
    if (slowr, slowc, slowdr, slowdc) == (fastr, fastc, fastdr, fastdc):
      return True
    in_bounds = fast_in_bounds
  return False

# This took several minutes to run, but it worked
# TODO: One idea to speed it up: Skip placing obstacles where the guard never walks

num_positions = 0
for r in range(num_rows):
  for c in range(num_cols):
    # print(f'({r}, {c})')
    if inp[r][c] in ['#', '^']:
      continue
    cand_array = deepcopy(inp)
    cand_array[r][c] = '#'
    if detect_loop(cand_array):
      num_positions += 1

print(num_positions)
