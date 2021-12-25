from itertools import repeat

with open('example.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

fishes = [int(x) for x in lines[0].split(',')]
# print(fishes)

def get_tomorrow(fs):
  tomorrow = []
  new_fishes = 0
  # print(f'fs: {fs}')
  for fish in fs:
    # print(f'fish, tomorrow: {fish}, {tomorrow}')
    if fish == 0:
      new_fishes += 1
      tomorrow.append(6)
    else:
      tomorrow.append(fish - 1)

  tomorrow.extend(repeat(8, new_fishes))
  return tomorrow

days = 0

while days < 80:
  days += 1
  fishes = get_tomorrow(fishes)
  # print(f'Day {days}: {fishes}')
  # fishes = next_fishes
  # quit()

print(len(fishes))
