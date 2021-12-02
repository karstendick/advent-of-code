with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

x,d = 0,0
for line in lines:
  command, units = line.split()
  units = int(units)
  if command == 'forward':
    x += units
  if command == 'down':
    d += units
  if command == 'up':
    d -= units

print(f'({x}, {d}): {x*d}')
