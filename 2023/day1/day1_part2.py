import re
inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())


digits_regex = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')

def str_to_int(string):
  if string == 'one':
    return 1
  if string == 'two':
    return 2
  if string == 'three':
    return 3
  if string == 'four':
    return 4
  if string == 'five':
    return 5
  if string == 'six':
    return 6
  if string == 'seven':
    return 7
  if string == 'eight':
    return 8
  if string == 'nine':
    return 9
  return int(string)

sum = 0
for line in inp:
  first_digit = re.findall(digits_regex, line)[0]
  last_digit = re.findall(digits_regex, line)[-1]
  num = 10*str_to_int(first_digit) + str_to_int(last_digit)
  sum += num



print(sum)
  
