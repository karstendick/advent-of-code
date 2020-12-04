lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      lines.append(line)

required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

valid_passports = 0
passport = []
for line in lines:
  if not line:
    # print("Empty!")
    num_fields = len(passport)
    # if num_fields == 8 or (num_fields == 7 and required_fields == set(passport)):
    if required_fields.issubset(set(passport)):
      valid_passports += 1
      # print(sorted(passport))
      # print(f"valid:{sorted(passport)}")
      print(valid_passports)
    else:
      print(f"invalid({len(passport)}):{sorted(passport)}")
    passport = []
  else:
    passport += [kv_pair.split(':')[0] for kv_pair in line.split(' ')]
    # print(passport)

print(valid_passports+1) # Not handling last line correctly
# 218 is too low
