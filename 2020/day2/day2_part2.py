valid_passwords = 0

with open('input.txt', 'r') as f:
    for line in f:
      min_max, letter_colon, password = line.split()
      pmin, pmax = [int(c) for c in min_max.split('-')]
      letter = letter_colon[0:1] # remove colon

      password = ' ' + password  # account for 1-indexing
      matching_chars = 0
      if password[pmin] == letter:
        matching_chars += 1
      if password[pmax] == letter:
        matching_chars += 1
      if matching_chars == 1: # exactly one match
        valid_passwords += 1

      # print(f"{pmin} | {pmax} | {letter} | {password} | {num_letters}")

print(valid_passwords)
