from collections import namedtuple
from itertools import product

Machine = namedtuple('Machine', ['ax', 'ay', 'bx', 'by', 'px', 'py'])

machines = []
with open('example.txt', 'r') as f:
  for line in f:
    line = line.strip()
    segments = line.replace('+', ' ').replace(',', ' ').replace('=', ' ').split()
    if line.startswith('Button A:'):
      ax = int(segments[3])
      ay = int(segments[5])
    elif line.startswith('Button B:'):
      bx = int(segments[3])
      by = int(segments[5])
    elif line.startswith('Prize:'):
      px = int(segments[2])
      py = int(segments[4])
      machine = Machine(ax, ay, bx, by, px, py)
      machines.append(machine)

# print(machines)

total_tokens = 0
for machine in machines:
  cand_tokens = []
  button_presses = list(product(range(101), range(101)))
  for (apresses, bpresses) in button_presses:
    clawx = machine.ax * apresses + machine.bx * bpresses
    clawy = machine.ay * apresses + machine.by * bpresses
    if clawx == machine.px and clawy == machine.py:
      tokens = 3 * apresses + 1 * bpresses
      cand_tokens.append(tokens)
  if cand_tokens:
    total_tokens += min(cand_tokens)

print(total_tokens)
