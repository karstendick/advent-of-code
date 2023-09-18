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

digit_to_num_segments = {
  0: 6,
  1: 2,
  2: 5,
  3: 5,
  4: 4,
  5: 5,
  6: 6,
  7: 3,
  8: 7,
  9: 6
}

digit_to_num_segments = {
  1: 2,
  7: 3,
  4: 4,

  2: 5,
  3: 5,
  5: 5,

  6: 6,
  0: 6,
  9: 6,

  8: 7
}

digits_to_segments = {
  0: {'a', 'b', 'c', 'e', 'f', 'g'},
  1: {'c', 'f'},
  2: {'a', 'c', 'd', 'e', 'g'},
  3: {'a', 'c', 'd', 'f', 'g'},
  4: {'b', 'c', 'd', 'f'},
  5: {'a', 'b', 'd', 'f', 'g'},
  6: {'a', 'b', 'd', 'e', 'f', 'g'},
  7: {'a', 'c', 'f'},
  8: {'a', 'b', 'c', 'd', 'e', 'f', 'g',},
  9: {'a', 'b', 'c', 'd', 'f', 'g'}
}
