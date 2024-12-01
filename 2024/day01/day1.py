inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append([int(num) for num in line.split()])

print(inp)

def transpose(matrix):
  return list(map(list, zip(*matrix)))

m = transpose(inp)
print(m)
m = [sorted(l) for l in m]
print(m)

dists = []
for i in range(len(m[0])):
  dists.append(abs(m[0][i] - m[1][i]))
print(dists)
total = sum(dists)
print(total)
