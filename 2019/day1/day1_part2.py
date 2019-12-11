
def calc_fuel(module_mass):
    fuel = module_mass//3 - 2
    if fuel <= 0:
        return 0

    return fuel + calc_fuel(fuel)

total_fuel = 0

with open('input.txt', 'r') as f:
    for line in f:
        module_mass = int(line)
        fuel = calc_fuel(module_mass)
        total_fuel += fuel

print(f'total_fuel: {total_fuel}')

import pdb; pdb.set_trace();
