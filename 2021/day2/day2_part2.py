with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

x,d,a = 0,0,0
for line in lines:
  command, units = line.split()
  units = int(units)
  if command == 'forward':
    x += units
    d += a * units
  if command == 'down':
    a += units
  if command == 'up':
    a -= units
  # print(f'{x}, {d}, {a}')

print(f'({x}, {d}): {x*d}')
