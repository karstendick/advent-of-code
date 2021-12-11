from itertools import repeat

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

# print(lines)
N = len(lines)

num_ones = list(repeat(0, len(lines[0])))

for line in lines:
  for i, c in enumerate(line):
    if int(c) == 1:
      num_ones[i] += 1

print(num_ones)
print(N)

most_digits = []
least_digits = []
for num in num_ones:
  if num > N/2:
    most_digits.append(1)
    least_digits.append(0)
  else:
    most_digits.append(0)
    least_digits.append(1)

most_str = ''.join([str(x) for x in most_digits])
least_str = ''.join([str(x) for x in least_digits])

gamma_rate = int(most_str, 2)
epsilon_rate = int(least_str, 2)

print(f'{gamma_rate} * {epsilon_rate} = {gamma_rate * epsilon_rate}')
