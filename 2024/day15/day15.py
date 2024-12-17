warehouse = []
moves = []
inp = []
with open('input.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if line.startswith('#'):
      warehouse.append(list(line))
    elif line and line[0] in '<>^v':
      moves.extend(line)

# print(warehouse)
# print(moves)

def find_index_2d(array, value):
  for r, row in enumerate(array):
    if value in row:
      return (r, row.index(value))
  return None

def swap(fromr, fromc, tor, toc):
  warehouse[fromr][fromc], warehouse[tor][toc] = warehouse[tor][toc], warehouse[fromr][fromc]

def get_cell(rc):
  r, c = rc
  return warehouse[r][c]

robotr, robotc = find_index_2d(warehouse, '@')

# print(f'({robotr}, {robotc})')

# NESW vectors
vs = {'^': (-1, 0),
      '>': (0, 1),
      'v': (1, 0),
      '<': (0, -1)}

def move_one(move):
  global robotr, robotc
  (dr, dc) = vs[move]
  targetr, targetc = robotr + dr, robotc + dc
  target_val = warehouse[targetr][targetc]
  if target_val == '.': # empty space
    swap(robotr, robotc, targetr, targetc)
    robotr, robotc = targetr, targetc
    return
  elif target_val == '#': # wall
    return
  elif target_val == 'O':
    ir, ic = targetr, targetc
    while warehouse[ir][ic] == 'O':
      ir, ic = ir + dr, ic + dc
    final_target_val = warehouse[ir][ic]
    if final_target_val == '.':
      swap(targetr, targetc, ir, ic) # put a box in that final space
      swap(targetr, targetc, robotr, robotc) # move the robot
      robotr, robotc = targetr, targetc
      return
    elif final_target_val == '#':
      return
  else:
    raise Exception(f'Unknown target value {target_val} at ({targetr}, {targetc})')
  
def print_warehouse():
  for row in warehouse:
    print(''.join(row))

for i, move in enumerate(moves):
  # print(f'Move #{i}: {move}')
  move_one(move)
  # print_warehouse()

total = 0
for r, row in enumerate(warehouse):
  for c, e in enumerate(row):
    if e == 'O':
      total += 100 * r + c

print(total)
