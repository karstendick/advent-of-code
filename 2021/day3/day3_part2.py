from itertools import repeat

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

# print(lines)
length = len(lines)

width = len(lines[0])

def get_most_rating(lines, is_most=1):
  for bit_pos in range(width):
    print(f'lines: {lines}')
    lines = get_most_rating_subset(lines, bit_pos=bit_pos, is_most=is_most)
    if len(lines) == 1:
      return lines[0]
  
  # num_ones = 0
  # for line in lines:
  #   if int(line[bit_pos]) == 1:
  #     num_ones += 1

  # if num_ones * 2 >= length:
  #   most_common_value = 1
  #   least_common_value = 0
  # else:
  #   most_common_value = 0
  #   least_common_value = 1

def get_most_rating_subset(lines, bit_pos=0, is_most=1):
  length = len(lines)
  num_ones = 0
  for line in lines:
    if int(line[bit_pos]) == 1:
      num_ones += 1

  
  if num_ones * 2 >= length:
    value = 1 if is_most==1 else 0
  else:
    value = 0 if is_most==1 else 1
  
  print(f'num_ones: {num_ones}, length: {length}, value: {value}')

  return [line for line in lines if int(line[bit_pos]) == value]

most_value_rating = get_most_rating(lines, 1)
# most_value_rating = 'foo'
least_value_rating = get_most_rating(lines, 0)

prod = int(most_value_rating, 2) * int(least_value_rating, 2)

print(f'{most_value_rating} * {least_value_rating} = {prod}')
# for line in lines:
#   for i, c in enumerate(line):
#     if int(c) == 1:
#       num_ones[i] += 1

# print(num_ones)
# print(N)

# most_digits = []
# least_digits = []
# for num in num_ones:
#   if num > N/2:
#     most_digits.append(1)
#     least_digits.append(0)
#   else:
#     most_digits.append(0)
#     least_digits.append(1)

# most_str = ''.join([str(x) for x in most_digits])
# least_str = ''.join([str(x) for x in least_digits])

# gamma_rate = int(most_str, 2)
# epsilon_rate = int(least_str, 2)

# print(f'{gamma_rate} * {epsilon_rate} = {gamma_rate * epsilon_rate}')
