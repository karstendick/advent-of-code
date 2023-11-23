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

sum = 0
for cyclei in [20,60,100,140,180,220]:
  sum += cycle_to_X[cyclei] * cyclei

print(f'sum: {sum}')
