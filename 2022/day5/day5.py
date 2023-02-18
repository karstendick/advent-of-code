inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.rstrip('\n'))

sepi = inp.index('')

box_input = inp[:sepi-1]
num_stacks = max(map(int, inp[sepi-1].split()))
moves = inp[sepi+1:]


print(box_input)
print()
print(num_stacks)
print()
print(moves)

stacks = [[] for i in range(num_stacks+1)]

for line in box_input[::-1]:
  print(line)
  for i in range(1, num_stacks+1):
    ch = line[1 + (i-1) * 4]
    if ch.strip():
      stacks[i].append(ch)

print(stacks)

def move_box(source, sink):
  box = stacks[source].pop()
  stacks[sink].append(box)

for move in moves:
  _, boxnum, _, source, _, sink = move.split()
  for i in range(int(boxnum)):
    move_box(int(source), int(sink))

tops = ''
for stack in stacks:
  if stack:
    box = stack.pop()
    tops += box

print(tops)


