from ast import literal_eval

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    if line.strip() == '':
      continue
    inp.append(literal_eval(line))

# print(inp)

def in_right_order(left, right):
  if isinstance(left, int) and isinstance(right, int):
    return left < right
  if isinstance(left, list) and isinstance(right, list):
    if len(left) == 0:
      return True
    if len(right) == 0:
      return False
    if left[0] == right[0]:
      return in_right_order(left[1:], right[1:])
    if isinstance(left[0], int) and isinstance(right[0], int):
      return left[0] < right[0]
    return in_right_order(left[0], right[0]) and in_right_order(left[1:], right[1:])
  if isinstance(left, int) and isinstance(right, list):
    return in_right_order([left], right)
  if isinstance(left, list) and isinstance(right, int):
    return in_right_order(left, [right])
  
  raise Exception(f'How did we get here? {left} | {right}')
  return False

pair_index = 1
pair_index_sum = 0
for i in range(0, len(inp), 2):
  left = inp[i]
  right = inp[i+1]

  if in_right_order(left, right):
    # print(f'{pair_index}: In the right order')
    pair_index_sum += pair_index
  else:
    # print(f'{pair_index}: Not in the right order')
    pass
  pair_index += 1

print(pair_index_sum)
# 371 is too low
