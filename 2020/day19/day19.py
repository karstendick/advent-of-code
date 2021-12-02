from re import fullmatch

with open('input.txt', 'r') as f:
  lines = [l.strip() for l in f.readlines()]

rules = []
strs = []
rulesd = {}
found_break = False
for line in lines:
  if line == '':
    found_break = True
    continue
  if not found_break:
    rules.append(line)
    rule_num, rule = line.split(':')
    rulesd[rule_num] = rule.strip().split(' ')
  else:
    strs.append(line)

print(rules)
print(strs)
print(rulesd)

def eval_rule(rule):
  # print(f"evaling rule: {rule}")
  if len(rule) == 1:
    if rule[0].startswith('"'):
      return rule[0][1]
    return eval_rule(rulesd[rule[0]])

  s = '(?:'
  for token in rule:
    if token == '|':
      s += token
    else:
      s += eval_rule([token])
  s += ')'
  return s

rule0re = eval_rule(rulesd['0'])
print(rule0re)

n=0
for s in strs:
  if fullmatch(rule0re, s):
    n += 1

print(n)