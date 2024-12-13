from math import floor, log10
from functools import cache

stones = []
with open('example.txt', 'r') as f:
  for line in f:
    stones.extend([int(x) for x in line.split()])

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


@cache
def blink_once(stones):
  new_stones = []
  for stone in stones:
    new_vals = get_new_vals(stone)
    new_stones.extend(new_vals)
  return tuple(new_stones)

@cache
def blink_n_times(stones, n):
  for i in range(n):
    print(f'Blink #{i+1}: {len(stones)} stones')
    stones = blink_once(stones)
  return stones

@cache
def stone_len(stone, blink_times):
  stones = tuple([stone])
  stones = blink_n_times(stones, blink_times)
  return len(stones)


blink_times = 6
total = 0
n = len(stones)
stones = tuple(stones)
for i, stone in enumerate(stones):
  l = stone_len(stone, blink_times)
  print(f'Stone #{i} becomes {l} stones')
  total += l

print(total)
