from itertools import repeat
from collections import defaultdict

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

fishes = [int(x) for x in lines[0].split(',')]
# print(fishes)

fish_counts = defaultdict(int)
for fish in fishes:
  fish_counts[fish] += 1

def get_tomorrow(fish_counts):
  # tomorrow = []
  new_fish_counts = defaultdict(int)
  # print(f'fs: {fs}')
  for num, fish_count in fish_counts.items():
    # print(f'fish, tomorrow: {fish}, {tomorrow}')
    if num == 0:
      new_fish_counts[8] = fish_count
      new_fish_counts[6] += fish_count
    else:
      new_fish_counts[num-1] += fish_count

  # tomorrow.extend(repeat(8, new_fishes))
  return new_fish_counts

days = 0

while days < 256:
  days += 1
  fish_counts = get_tomorrow(fish_counts)
  # print(f'Day {days}: {fish_counts}')
  # fishes = next_fishes
  # quit()

print(fish_counts)
total = 0
for _, fish_count in fish_counts.items():
  total += fish_count
print(total)
