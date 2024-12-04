from copy import deepcopy

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append([int(num) for num in line.split()])

# print(inp)

def is_safe(l):
  is_inc = (l[1] - l[0] > 0)
  for i in range(1,len(l)):
    diff = l[i] - l[i-1]
    if diff == 0:
      return False, i
    if is_inc and diff < 0:
      return False, i
    if not is_inc and diff > 0:
      return False, i
    if abs(diff) > 3:
      return False, i
  return True, None

def is_safe_without_one_level(l):
  origl = deepcopy(l)
  origl2 = deepcopy(l)
  is_safe_already, i = is_safe(l)
  # print(f'is_safe_already, i: {is_safe_already}, {i}')
  if is_safe_already:
    return True

  del l[i]
  # print(f'l | is_safe: {l} | {is_safe(l)}')
  if is_safe(l)[0]:
    return True

  del origl[i-1]
  if is_safe(origl)[0]:
    return True
  
  del origl2[0]
  if is_safe(origl2)[0]:
    return True
  return False
  

num_safe = 0
for report in inp:
  if is_safe_without_one_level(report):
    # print(f'SAFE: {report}')
    num_safe += 1
  else:
    # print(f'UNSAFE: {report}')
    pass

print(num_safe)
