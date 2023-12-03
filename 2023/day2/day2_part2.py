inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

# print(inp)

# only 12 red cubes, 13 green cubes, and 14 blue cubes
maxes = {'red': 12, 'green': 13, 'blue': 14}

possible_games_sum = 0
game_num = 1
for line in inp:
  game_valid = True
  game_str = line.split(':')[1].strip()
  grabs = game_str.split(';')
  for grab in grabs:
    subsets = grab.split(',')
    for subset in subsets:
      num, color = subset.strip().split(' ')
      color = color.strip()
      num = int(num.strip())
      if num > maxes[color]:
        # print(f'Game {game_num} has too many {color} cubes')
        game_valid = False
        break
  if game_valid:
    possible_games_sum += game_num
  game_num += 1



print(possible_games_sum)
  
