inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append([int(c) for c in line.strip()])

# print(inp)

total_joltage = 0
for bank in inp:
    max_tens = 0
    max_ones = 0
    for i in range(len(bank) - 1):
        battery = bank[i]
        if battery > max_tens:
            max_tens = battery
            max_ones = 0
        elif battery > max_ones:
            max_ones = battery
    # handle last battery in the bank
    battery = bank[-1]
    if battery > max_ones:
        max_ones = battery
    max_joltage = max_tens * 10 + max_ones
    total_joltage += max_joltage

print(total_joltage)
