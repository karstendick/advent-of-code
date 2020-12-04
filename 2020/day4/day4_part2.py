def valid_hgt(hgt):
  unit = hgt[-2:]
  if unit not in ['in', 'cm']:
    return False
  height = int(hgt[0:-2])
  if unit == 'in':
    return 59 <= height <= 76
  if unit == 'cm':
    return 150 <= height <= 193

def valid_hcl(hcl):
  if hcl[0] != '#':
    return False
  num = hcl[1:]
  if len(num) != 6:
    return False
  for c in num:
    if c not in '0123456789abcdef':
      return False
  return True

def valid_ecl(ecl):
  return ecl in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def valid_pid(pid):
  if len(pid) != 9:
    return False
  for c in pid:
    if c not in '0123456789':
      return False
  return True

lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      lines.append(line)

required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

valid_passports = 0
passport = {}
for line in lines:
  if not line:
    num_fields = len(passport)
    if required_fields.issubset(set(passport))\
      and 1920 <= int(passport['byr']) <= 2002\
      and 2010 <= int(passport['iyr']) <= 2020\
      and 2020 <= int(passport['eyr']) <= 2030\
      and valid_hgt(passport['hgt'])\
      and valid_hcl(passport['hcl'])\
      and valid_ecl(passport['ecl'])\
      and valid_pid(passport['pid']):
      valid_passports += 1
      print(passport)
      # print(f"valid:{sorted(passport)}")
      print(valid_passports)
    else:
      print(f"invalid({len(passport)}):{sorted(passport)}")
    passport = {}
  else:
    passport.update({kv_pair.split(':')[0]: kv_pair.split(':')[1] for kv_pair in line.split(' ')})
    # print(passport)

print(valid_passports)
