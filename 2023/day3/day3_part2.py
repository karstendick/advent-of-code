inp = []
with open('example.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

# print(inp)

num_tuples = []

for r, line in enumerate(inp):
  num_str = ''
  cstart = None
  cend = None
  for c, char in enumerate(line):
    if char.isdigit():
      num_str += str(char)
      if cstart is None:
        cstart = c
    else:
      if num_str != '':
        num = int(num_str)
        cend = c - 1
        num_tuples.append((r, cstart, cend, num))

        num_str = ''
        cstart = None
        cend = None

# print(num_tuples)

def is_part_num(num_tuple):
  r, cstart, cend, num = num_tuple
  adj_chars = []
  if r > 0:
    adj_chars.extend(inp[r-1][cstart:cend+1])
  if cstart > 0:
    adj_chars.append(inp[r][cstart-1])
  if cend < len(inp[r]) - 1:
    adj_chars.append(inp[r][cend+1])
  if r < len(inp) - 1:
    adj_chars.extend(inp[r+1][cstart:cend+1])

  if r > 0 and cstart > 0:
    adj_chars.append(inp[r-1][cstart-1])
  if r > 0 and cend < len(inp[r]) - 1:
    adj_chars.append(inp[r-1][cend+1])
  if r < len(inp) - 1 and cstart > 0:
    adj_chars.append(inp[r+1][cstart-1])
  if r < len(inp) - 1 and cend < len(inp[r]) - 1:
    adj_chars.append(inp[r+1][cend+1])
  
  print(f'num: {num} | adj_chars: {adj_chars}')
  for char in adj_chars:
    if char.isdigit() or char == '.':
      continue
    return True
  return False

sum = 0
for num_tuple in num_tuples:
  if is_part_num(num_tuple):
    sum += num_tuple[3]

print(sum)
# 538293 is too low

