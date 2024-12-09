from operator import add, mul
from itertools import product

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append([int(x) for x in line.strip().replace(':', '').split()])

# print(inp)

def concat(x, y):
  return int(str(x) + str(y))

ops = [add, mul, concat]

def is_true(eq, ops):
  test_val = eq[0]
  acc = eq[1]
  ops_i = 0
  for i in range(2, len(eq)):
    # print(f'{ops[ops_i]}({acc, eq[i]})')
    acc = ops[ops_i](acc, eq[i])
    # print(f'acc: {acc}')
    ops_i += 1
  return acc == test_val

total = 0
for eq in inp:
  # print(eq)
  num_ops = len(eq) - 2
  cand_ops = product(ops, repeat=num_ops)
  for cand_op in cand_ops:
    # print(cand_op)
    if is_true(eq, cand_op):
      total += eq[0]
      break

print(total)
