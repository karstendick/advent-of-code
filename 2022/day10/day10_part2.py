inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

instructions = []
for line in inp:
  instruction = line.split()
  if len(instruction) == 2:
    instruction[1] = int(instruction[1])
  instructions.append(instruction)

# print(instructions)

X = 1
cycle = 0
cycle_to_X = {}
cycle_to_X[0] = 1

for inst in instructions:
  # print(f'During cycle {cycle}, X is {X}')
  if inst[0] == 'noop':
    cycle += 1
    cycle_to_X[cycle] = X
  elif inst[0] == 'addx':
    operand = inst[1]
    
    cycle += 1
    cycle_to_X[cycle] = X
    cycle += 1
    cycle_to_X[cycle] = X
    
    X += operand
  else:
    raise Exception("Unexpected instruction!")
  
  # cycle_to_X.append(X)
# print(f'After cycle {cycle}, X is {X}')
cycle_to_X[cycle+1] = X
# print(cycle_to_X)

crt = ['.' for i in range(245)]
for cycle in range(1,241):
  X = cycle_to_X[cycle]
  pixel_pos = (cycle-1)
  if (pixel_pos % 40) in [X-1, X, X+1]:
    # print(f'In cycle {cycle}, drawing pixel # in position {cycle-1} with X={X} & sprite=[{X-1}, {X}, {X+1}]')
    crt[pixel_pos] = '#'
  else:
    # print(f'In cycle {cycle}, drawing pixel . in position {cycle-1} with X={X} & sprite=[{X-1}, {X}, {X+1}]')
    pass

print(''.join(crt[0:40]))
print(''.join(crt[40:80]))
print(''.join(crt[80:120]))
print(''.join(crt[120:160]))
print(''.join(crt[160:200]))
print(''.join(crt[200:240]))
