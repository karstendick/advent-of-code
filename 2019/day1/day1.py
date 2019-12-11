
total_fuel = 0

with open('input.txt', 'r') as f:
    for line in f:
        module_mass = int(line)
        fuel = module_mass//3 - 2
        total_fuel += fuel

print(f'total_fuel: {total_fuel}')
