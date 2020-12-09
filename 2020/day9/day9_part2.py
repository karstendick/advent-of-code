from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

lines = []
with open('example_input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      lines.append(int(line))

window = 5 # 25
for i, num in enumerate(lines):
    if i < window:
        continue
    found_sum = False
    for xi, x in enumerate(lines[i-window:i]):
        for yi, y in enumerate(lines[i-window:i]):
            if xi == yi:
                continue
            if x + y == lines[i]:
                found_sum = True
    if not found_sum:
        print(lines[i])
