stones = []
with open('input.txt', 'r') as f:
  for line in f:
    stones.extend([int(x) for x in line.split()])

# print(stones)

def num_digits(n):
  return len(str(n))

def split_num(n):
  mid = len(str(n))//2
  left = int(str(n)[0:mid])
  right = int(str(n)[mid:])
  return left, right

def blink_once(stones):
  i = 0
  while i < len(stones):
    stone = stones[i]
    if stone == 0:
      stones[i] = 1
    elif num_digits(stone) % 2 == 0:
      left, right = split_num(stone)
      stones[i] = left
      stones.insert(i+1, right)
      i += 1
    else:
      stones[i] = 2024 * stone

    i += 1
  return stones

def blink_n_times(stones, n):
  for _ in range(n):
    stones = blink_once(stones)
  return stones

stones = blink_n_times(stones, 25)
# print(stones)
print(len(stones))
