inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

print(inp)

sum = 0
for line in inp:
  first_digit = next((x for x in line if x.isdigit()), None)
  last_digit = next((x for x in reversed(line) if x.isdigit()), None)
  num = int(f'{first_digit}{last_digit}')
  sum += num



print(sum)
  
