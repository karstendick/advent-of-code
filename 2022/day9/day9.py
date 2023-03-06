inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

motions = []
for line in inp:
  dir, n = line.split()
  motions.append([dir, int(n)])

print(motions)

hx, hy = 0, 0
tx, ty = 0, 0

def move_head(dir, n):
  global hx, hy
  if dir == 'R':
    hx += n
  elif dir == 'L':
    hx -= n
  elif dir == 'U':
    hy += n
  elif dir == 'D':
    hy -= n
  else:
    raise Exception(f"received invalid direction {dir}")

def sgn(x):
  if x > 0:
    return 1
  elif x < 0:
    return -1
  else:
    return 0

def move_tail():
  global tx, ty
  dx = hx - tx
  dy = hy - ty
  if abs(dx) <= 1 and abs(dy) <= 1:
    return
  elif abs(dx) == 2 and abs(dy) == 0:
    if dx == 2:
      tx += 1
    elif dx == -2:
      tx -= 1
  elif abs(dx) == 0 and abs(dy) == 2:
    if dy == 2:
      ty += 1
    elif dy == -2:
      ty -= 1
  else:
    # print(f"Moving tail diagonally: ({sgn(dx)},{sgn(dy)})")
    tx += sgn(dx)
    ty += sgn(dy)
  
tail_positions = set()
tail_positions.add((tx, ty))
for motion in motions:
  dir, n = motion
  for i in range(n):
    move_head(dir, 1)
    move_tail()
    tail_positions.add((tx, ty))

  # print(f"{motion} to H: ({hx},{hy}) T: ({tx},{ty})")

# print(tail_positions)
print(len(tail_positions))









