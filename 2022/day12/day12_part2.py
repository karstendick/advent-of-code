from operator import add, mul

class Monkey:
  def __init__(self, number, items, operator, leftop, rightop, divisor, true_target, false_target):
    self.number = number
    self.items = items
    self.operator = operator
    self.divisor = divisor
    self.leftop = leftop
    self.rightop = rightop
    self.true_target = true_target
    self.false_target = false_target
    self.num_inspections = 0
  def __repr__(self):
    return f'Monkey {self.number} with items {self.items} and operator {self.operator} and divisor {self.divisor} and leftop {self.leftop} and rightop {self.rightop} and true_target {self.true_target} and false_target {self.false_target}'


inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

monkeys = []

num = 0
items = []
operator = None
divisor = None
leftop = None
rightop = None
true_target = None
false_target = None
for line in inp:
  if line.startswith('Monkey'):
    num = int(line.split(' ')[1].rstrip(':'))
  elif line.startswith('Starting items'):
    items = [int(x) for x in line.split(':')[1].split(',')]
  elif line.startswith('Operation'):
    line = line.split(':')[1].strip()
    _,_,leftop, operator, rightop = line.split(' ')
  elif line.startswith('Test'):
    divisor = int(line.split(' ')[-1])
  elif line.startswith('If true'):
    true_target = int(line.split(' ')[-1])
  elif line.startswith('If false'):
    false_target = int(line.split(' ')[-1])
    monkeys.append(Monkey(num, items, operator, leftop, rightop, divisor, true_target, false_target))

# print(monkeys)


# calculate product of a list of numbers
def prod(numbers):
  p = 1
  for n in numbers:
    p *= n
  return p

divisor_product = prod([monkey.divisor for monkey in monkeys])

def calc_operation(item, monkey):
  if monkey.operator == '*':
    operator = mul
  elif monkey.operator == '+':
    operator = add
  else:
    raise Exception(f'Unknown operator {monkey.operator}')
  if monkey.leftop == 'old':
    left = item
  else:
    left = int(monkey.leftop)
  if monkey.rightop == 'old':
    right = item
  else:
    right = int(monkey.rightop)
  return operator(left, right)

def take_one_turn(monkeys, i):
  monkey = monkeys[i]
  while len(monkey.items) != 0:
    monkey.num_inspections += 1
    item = monkey.items.pop(0)
    item = calc_operation(item, monkey)
    # item = item // 3 # worry no longer decreases!
    item = item % divisor_product # we're in Z_{divisor_product}!

    if item % monkey.divisor == 0:
      monkeys[monkey.true_target].items.append(item)
    else:
      monkeys[monkey.false_target].items.append(item)
  return monkeys

def one_round(monkeys):
  for i in range(len(monkeys)):
    monkeys = take_one_turn(monkeys, i)
  return monkeys



# take 10000 rounds
for i in range(10000):
  if i % 100 == 0:
    print(f'Round {i}')
  monkeys = one_round(monkeys)

# caulcate the top 2 integers from a list
def top_two(items):
  top1 = 0
  top2 = 0
  for item in items:
    if item > top1:
      top2 = top1
      top1 = item
    elif item > top2:
      top2 = item
  return top1, top2

top1, top2 = top_two([monkeys[i].num_inspections for i in range(len(monkeys))])
monkey_biz = top1 * top2
print(f'Monkey biz is {monkey_biz}')
