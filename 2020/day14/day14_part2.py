from collections import deque

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

# print(lines)

def apply_mask(mask, index):
  index_bstr = format(index, '036b')
  ret = ''
  for i, d in enumerate(index_bstr):
    if mask[i] == 'X':
      ret += 'X'
    elif mask[i] == '1':
      ret += '1'
    elif mask[i] == '0':
      ret += d
    else:
      raise Exception("Illegal digit!")
  return ret

def masked_index_to_indexes(masked_index):
  q = deque([masked_index])
  while q:
    e = q.popleft()
    if 'X' in e:
      i = e.find('X')
      left = e[:i] + '0' + e[i + 1:]
      right = e[:i] + '1' + e[i + 1:]
      q.append(left)
      q.append(right)
    else:
      yield e



mem = {}
mask = None
for line in lines:
  if line.startswith('mask'):
    mask = line.split(' = ')[1]
  else:
    loc, value = line.split(' = ')
    value = int(value)
    index = int(loc.strip('mem[]'))
    masked_index = apply_mask(mask, index)
    # print(f"{index} | {value} | {masked_index}")
    for index in masked_index_to_indexes(masked_index):
      # print(index)
      index_int = int(index, 2)
      mem[index_int] = value

print(sum(mem.values()))
