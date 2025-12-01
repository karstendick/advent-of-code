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
    dial = (dial - distance) % N
  elif direction == 'R':
    dial = (dial + distance) % N
  else:
    raise ValueError(f'Invalid direction: {direction}')
  if dial == 0:
    num_zeroes += 1

print(f'{num_zeroes}')
