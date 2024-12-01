from collections import Counter

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append([int(num) for num in line.split()])

# print(inp)

def transpose(matrix):
  return list(map(list, zip(*matrix)))

m = transpose(inp)
# print(m)

left, right = m
# print(left, right)

right_freq = Counter(right)
# print(right_freq)

scores = []
for e in left:
  score = e * right_freq[e]
  scores.append(score)

# print(scores)
total = sum(scores)
print(total)
