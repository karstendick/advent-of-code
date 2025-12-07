from operator import add, mul
from functools import reduce

inp = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        items = line.split()
        if not ('*' in items or '+' in items):
            items = [int(x) for x in items]
        inp.append(items)

# print(inp)

num_cols = len(inp[0])
num_rows = len(inp)
total = 0
for i in range(num_cols):
    op = inp[-1][i]
    nums = [inp[j][i] for j in range(num_rows - 1)]
    if op == '*':
        total += reduce(mul, nums)
    elif op == '+':
        total += reduce(add, nums)

print(total)
