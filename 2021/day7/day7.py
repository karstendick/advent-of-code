with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

crabs = [int(x) for x in lines[0].split(',')]
min_crab = min(crabs)
max_crab = max(crabs)
# print(f'{crabs}, {min_crab}, {max_crab}')

def get_fuel(crabs, pos):
  fuel = 0
  for crab in crabs:
    fuel += abs(crab - pos)
  return fuel

min_fuel = None
for pos in range(min_crab, max_crab+1):
  fuel = get_fuel(crabs, pos)
  # print(f'pos, fuel: {pos}, {fuel}')
  if not min_fuel or fuel < min_fuel:
    min_fuel = fuel

print(min_fuel)
