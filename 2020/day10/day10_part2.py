from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = list(map(int, f))

adapters = sorted(lines)
adapters_set = set(adapters)

paths = defaultdict(int)
paths[0] = 1
adapters = [0] + adapters
for adapter in adapters:
    for diff in range(1,4):
        next_adapter = adapter + diff
        if next_adapter in adapters_set:
            paths[next_adapter] += paths[adapter]

print(paths[adapters[-1]])
