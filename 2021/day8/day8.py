with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

count = 0
for line in lines:
  _, output_str = line.split('|')
  output_vals = output_str.split()
  for output_val in output_vals:
    n = len(output_val)
    if n in [2, 3, 4, 7]:
      count += 1

print(count)
