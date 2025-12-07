from operator import add, mul
from functools import reduce

inp = []
with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.strip('\n'))

# print(inp)

def get_op_indexes(op_line):
    return [i for i, c in enumerate(op_line) if c in ['*', '+']] + [len(op_line)]

op_indexes = get_op_indexes(inp[-1])
# print(op_indexes)


def get_nums_by_col(num_strs):
    for c in range(len(num_strs[0])):
        num_str = ''
        for r in range(len(num_strs)):
            num_str += num_strs[r][c]
        num_str = num_str.strip()
        if num_str != '':
            yield int(num_str)

num_cols = len(inp[0])
num_rows = len(inp)
total = 0
for i in range(len(op_indexes) - 1):
    op_index = op_indexes[i]
    end_index = op_indexes[i+1]
    op = inp[-1][op_index]
    num_strs = [inp[j][op_index:end_index] for j in range(num_rows - 1)]
    # print(f'op: {op}, num_strs: {num_strs}')
    nums = list(get_nums_by_col(num_strs))
    # print(f'nums: {nums}')
    if op == '*':
        total += reduce(mul, nums)
    elif op == '+':
        total += reduce(add, nums)

print(total)
