from collections import namedtuple
from itertools import product
from sympy import symbols, Eq, solve

Machine = namedtuple('Machine', ['ax', 'ay', 'bx', 'by', 'px', 'py'])

ten_trillion = 10_000_000_000_000

machines = []
with open('input.txt', 'r') as f:
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
      px = int(segments[2]) + ten_trillion
      py = int(segments[4]) + ten_trillion
      machine = Machine(ax, ay, bx, by, px, py)
      machines.append(machine)

# print(machines)

total_tokens = 0
for machine in machines:
  a, b = symbols('a b', integer=True)
  eq1 = Eq(machine.ax * a + machine.bx * b, machine.px)
  eq2 = Eq(machine.ay * a + machine.by * b, machine.py)
  soln = solve((eq1, eq2), (a, b))
  if soln:
    apresses, bpresses = soln[a], soln[b]
    tokens = 3 * apresses + 1 * bpresses
    total_tokens += tokens

print(total_tokens)
