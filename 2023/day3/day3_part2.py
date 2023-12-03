import re

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

# print(inp)
unique_chars = set()
for line in inp:
  unique_chars.update(line)

# print(f'unique_chars: {sorted(unique_chars)}')


num_tuples = []

for r, line in enumerate(inp):
  num_str = ''
  cstart = None
  cend = None
  for c, char in enumerate(line):
    if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    # if char.isdigit():
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
  # this part is key to get a number at the end of a line
  if num_str != '':
    num = int(num_str)
    cend = c
    num_tuples.append((r, cstart, cend, num))

# print(num_tuples)

def is_part_num(num_tuple):
  r, cstart, cend, num = num_tuple
  adj_chars = []
  if r > 0:
    # up
    adj_chars.extend(inp[r-1][cstart:cend+1])
  if cstart > 0:
    # left
    adj_chars.append(inp[r][cstart-1])
  if cend < len(inp[r]) - 1:
    # right
    adj_chars.append(inp[r][cend+1])
  if r < len(inp) - 1:
    # down
    adj_chars.extend(inp[r+1][cstart:cend+1])

  if r > 0 and cstart > 0:
    # up left
    adj_chars.append(inp[r-1][cstart-1])
  if r > 0 and cend < len(inp[r]) - 1:
    # up right
    adj_chars.append(inp[r-1][cend+1])
  if r < len(inp) - 1 and cstart > 0:
    # down left
    adj_chars.append(inp[r+1][cstart-1])
  if r < len(inp) - 1 and cend < len(inp[r]) - 1:
    # down right
    adj_chars.append(inp[r+1][cend+1])
  
  # print(f'num: {num} | adj_chars: {adj_chars}')

  for char in adj_chars:
    if char in ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']:
      return True
    # check if char is a digit:
    # if re.match(r'\d', char) or char == '.':
    # if char.isdigit() or char == '.':
    #   continue
    # return True
  return False

sum = 0
part_nums = []
non_part_nums = []
non_part_num_tuples = []
for num_tuple in num_tuples:
  num = num_tuple[3]
  if is_part_num(num_tuple):
    sum += num
    part_nums.append(num)
  else:
    non_part_nums.append(num)
    non_part_num_tuples.append(num_tuple)

# print(f'part_nums: {part_nums}')
# print(f'non_part_num_tuples: {non_part_num_tuples}')
# for non_part_num_tuple in non_part_num_tuples:
#   r, cstart, cend, num = non_part_num_tuple
#   print(f'num: {num} | r: {r} | cstart: {cstart} | cend: {cend}')
  
print(sum)
