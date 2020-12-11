from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = list(map(int, f))

adapters = sorted(lines)

joltage = 0
diffs = defaultdict(int)

for adapter in adapters:
    diff = adapter - joltage
    diffs[diff] += 1
    joltage += diff

diffs[3] += 1

print(diffs)

print(diffs[1] * diffs[3])