from math import prod

positions = []
velocities = []
with open('input.txt', 'r') as f:
  for line in f:
    segments = line.replace('=', ' ').replace(',', ' ').split()
    print(segments)
    positions.append((int(segments[1]), int(segments[2])))
    velocities.append((int(segments[4]), int(segments[5])))

# print(positions)
# print(velocities)

xmax = 101
ymax = 103
# for example only:
# xmax = 11
# ymax = 7

num_seconds = 100

new_positions = []
for i in range(len(positions)):
  x = (positions[i][0] + num_seconds * velocities[i][0]) % xmax
  y = (positions[i][1] + num_seconds * velocities[i][1]) % ymax
  new_positions.append((x, y))

# print(new_positions)

def get_quadrant(pos):
  x, y = pos
  if x < xmax//2:
    if y < ymax//2:
      return 1
    elif y > ymax//2:
      return 2
    else:
      return 0
  elif x > xmax//2:
    if y < ymax//2:
      return 3
    elif y > ymax//2:
      return 4
  return 0

quadrant_factor = [0]*5
for pos in new_positions:
  quad = get_quadrant(pos)
  quadrant_factor[quad] += 1

# print(quadrant_factor)
safety_factor = prod(quadrant_factor[1:])
print(safety_factor)
