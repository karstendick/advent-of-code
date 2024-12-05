from collections import defaultdict

before_to_after = defaultdict(set)
after_to_before = defaultdict(set)
updates = []
with open('input.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if '|' in line:
      before, after = [int(x) for x in line.split('|')]
      before_to_after[before].add(after)
      after_to_before[after].add(before)
    elif ',' in line:
      update = [int(x) for x in line.split(',')]
      updates.append(update)

# print(before_to_after)
# print(after_to_before)
# print(updates)

def is_ordered(update):
  for i, page in enumerate(update):
    befores = set(update[0:i])
    afters = set(update[i+1:])
    if not afters.isdisjoint(after_to_before[page]):
      return False
    # I think this check is redundant:
    if not befores.isdisjoint(before_to_after[page]):
      return False
  return True

total = 0
for update in updates:
  if is_ordered(update):
    middle_page_num = update[len(update) // 2]
    total += middle_page_num
    # print(f'ORDERED: {update}')
  else:
    # print(f'UNORDERED: {update}')
    pass

print(total)
