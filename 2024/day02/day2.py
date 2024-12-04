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
      return False
    if is_inc and diff < 0:
      return False
    if not is_inc and diff > 0:
      return False
    if abs(diff) > 3:
      return False
  return True

num_safe = 0
for report in inp:
  if is_safe(report):
    # print(f'SAFE: {report}')
    num_safe += 1
  else:
    # print(f'UNSAFE: {report}')
    pass

print(num_safe)
