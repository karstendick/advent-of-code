inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append((line[0], int(line[1:])))

# print(inp)

N = 100
dial = 50
num_zeroes = 0
for (direction, distance) in inp:
  if direction == 'L':
    diff = -1
  elif direction == 'R':
    diff = 1
  else:
    raise ValueError(f'Invalid direction: {direction}')

  for i in range(distance):
    dial = (dial + diff) % N
    if dial == 0:
      num_zeroes += 1

print(f'{num_zeroes}')
