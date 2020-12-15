with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

print(lines)

def apply_mask(mask, value):
  value_bstr = format(value, '036b')
  mask_reverse = list(reversed(mask))
  ret = ''
  for i, d in enumerate(reversed(value_bstr)):
    if mask_reverse[i] == 'X':
      ret += d
    else:
      ret += mask_reverse[i]
  return ret[::-1] # reverse it back


mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
value = 11
print(apply_mask(mask, value))

mem = {}
mask = None
for line in lines:
  if line.startswith('mask'):
    mask = line.split(' = ')[1]
    # print(mask)
  else:
    loc, value = line.split(' = ')
    value = int(value)
    index = int(loc.strip('mem[]'))
    print(f"{index} | {value}")
    mem[index] = int(apply_mask(mask, value), 2)

print(sum(mem.values()))
