inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())


power_sum = 0
game_num = 1
for line in inp:
  game_valid = True
  game_str = line.split(':')[1].strip()
  grabs = game_str.split(';')
  current_maxes = {'red': 0, 'green': 0, 'blue': 0}
  for grab in grabs:
    subsets = grab.split(',')
    for subset in subsets:
      num, color = subset.strip().split(' ')
      color = color.strip()
      num = int(num.strip())
      if num > current_maxes[color]:
        current_maxes[color] = num
  power = current_maxes['red'] * current_maxes['green'] * current_maxes['blue']
  power_sum += power
  game_num += 1


print(power_sum)
