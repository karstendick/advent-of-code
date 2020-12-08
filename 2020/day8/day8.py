lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      lines.append(line)

visited_indexes = set()
index = 0
acc = 0
while True:
  if index in visited_indexes:
    print(acc)
    break
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
