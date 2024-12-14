from math import floor, log10
from functools import cache
from collections import Counter

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.extend([int(x) for x in line.split()])

# print(stones)

@cache
def num_digits(n):
  if n == 0:
    return 1
  return floor(log10(n)) + 1

@cache
def split_num(n, ndigits):
  split_point = 10 ** (ndigits // 2)
  left = n // split_point
  right = n % split_point
  return left, right

@cache
def get_new_vals(stone_val):
   if stone_val == 0:
      return [1]
   ndigits = num_digits(stone_val)
   if ndigits % 2 == 0:
      left, right = split_num(stone_val, ndigits)
      return [left, right]
   return [stone_val * 2024]


def blink_once(stones):
  new_stones = Counter()
  for stone, count in stones.items():
    for new_stone in get_new_vals(stone):
      new_stones[new_stone] += count
  return new_stones


blink_times = 75
stones = Counter(inp)
for i in range(1, blink_times + 1):
  stones = blink_once(stones)

print(sum(stones.values()))
