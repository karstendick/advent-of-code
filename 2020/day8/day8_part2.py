from copy import deepcopy

lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      lines.append(line)

def run_program(lines):
  visited_indexes = set()
  index = 0
  acc = 0
  exit_index = len(lines)
  while True:
    if index == exit_index:
      return acc
    if index in visited_indexes:
      return None
    visited_indexes.add(index)
    line = lines[index]
    operator, operand = line.split(' ')
    operand = int(operand)
    if operator == 'acc':
      acc += operand
      index += 1
    elif operator == 'jmp':
      index += operand
    elif operator == 'nop':
      index += 1
    else:
      raise Exception(f"Invalid operator: {operator}")

for i, line in enumerate(lines):
  program = deepcopy(lines)
  if line.startswith('jmp'):
    program[i] = line.replace('jmp', 'nop')
  elif line.startswith('nop'):
    program[i] = line.replace('nop', 'jmp')
  else:
    continue
  ret = run_program(program)
  if ret:
    print(ret)
    break
