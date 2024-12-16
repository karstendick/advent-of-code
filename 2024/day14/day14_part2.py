from collections import Counter

positions = []
velocities = []
with open('input.txt', 'r') as f:
  for line in f:
    segments = line.replace('=', ' ').replace(',', ' ').split()
    positions.append((int(segments[1]), int(segments[2])))
    velocities.append((int(segments[4]), int(segments[5])))

xmax = 101
ymax = 103
# for example only:
# xmax = 11
# ymax = 7

def area_to_str(positions):
  s = ''
  robots_by_pos = Counter(positions)
  area = [[0 for _ in range(ymax)] for _ in range(xmax)]
  for x in range(xmax):
    for y in range(ymax):
      area[x][y] = robots_by_pos[(x, y)]
  for y in range(ymax):
    for x in range(xmax):
      if area[x][y] == 0:
        s += '.'
      else:
        s += str(area[x][y])
    s += '\n'
  return s

def run_length_encoding(s):
    runs = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            runs += 1
    return runs

def calc_new_positions(num_seconds):
  new_positions = []
  for i in range(len(positions)):
    x = (positions[i][0] + num_seconds * velocities[i][0]) % xmax
    y = (positions[i][1] + num_seconds * velocities[i][1]) % ymax
    new_positions.append((x, y))
  return new_positions

rles = {}
for num_seconds in range(xmax*ymax):
  print(f'num_seconds={num_seconds}:')
  new_positions = calc_new_positions(num_seconds)
  s = area_to_str(new_positions)
  rles[num_seconds] = run_length_encoding(s)

min_key = min(rles, key=rles.get)
print(min_key)
s = area_to_str(calc_new_positions(min_key))
print(s)
print(min_key)

# max_key = max(rles, key=rles.get)
# print(max_key)
# s = area_to_str(calc_new_positions(max_key))
# print(s)
# print(max_key)
