import string
from operator import add, mul

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

def strip_ws(s):
  return s.translate(str.maketrans('', '', string.whitespace))
lines = [strip_ws(line) for line in lines]

print(lines)

def tokenize(line):
  l = []
  for c in line:
    if c.isdigit():
      l.append(int(c))
    else:
      l.append(c)
  return l

lines = [tokenize(line) for line in lines]

print(lines)

def rp_index(tokens):
  open_parens = 1
  for i, token in enumerate(tokens):
    if token == '(':
      open_parens += 1
    elif token == ')':
      open_parens -= 1
      if open_parens == 0:
        return i+1
  raise Exception(f"Expected to find a matching ). Make it to the end instead: {tokens}")

def get_func(op):
  if op == '+':
    return add
  if op == '*':
    return mul
  raise Exception(f"Expected op (+ or *), but got {op} instead")

def eval(s):
  print(f"EVAL: {s}")
  if len(s) == 1:
    return s[0]
  
  if s[0] == '(':
    rpi = rp_index(s[1:])
    if rpi == len(s)+1:
      return eval(s[1:rpi])
    l = eval(s[1:rpi])
    return eval([l]+s[rpi+1:])
  else:
    l = s[0]
    op = s[1]
    func = get_func(op)
    if s[2] == '(':
      rpi = rp_index(s[3:])
      print(f"JOSHUA rpi: {rpi} | About to eval: {s[3:rpi+2]}")
      r = eval(s[3:rpi+2])
      return eval([func(l, r)]+s[rpi+3:])
    else:
      r = s[2]
      func = get_func(op)
      return eval([func(l,r)] + s[3:])


# print(eval(lines[0]))

def print_eq(eq):
  print(f"eq:\n{eq}")
  print(f"{eval(tokenize(eq))}\n")

print_eq('2*3')
print_eq('1+2*3+4*5+6')
print_eq('(1+2)')
print_eq('3*(1+2)')
print_eq('1+(2*3)+(4*(5+6))')
print_eq('5+(8*3+9+3*4*3)')
print_eq('5*9*(7*3*3+9*3+(8+6*4))')
print_eq('((2+4*9)*(6+9*8+6)+6)+2+4*2')

s = 0
for line in lines:
  s += eval(line)

print(s)
