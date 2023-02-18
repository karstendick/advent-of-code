inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

# print(inp)

def get_compartments(rucksack):
  n = len(rucksack)
  # print(f"{n} | {rucksack}")
  return rucksack[:n//2], rucksack[n//2:]

def get_shared_item(comp1, comp2):
  return set(comp1).intersection(set(comp2)).pop()

def get_priority(item):
  if item.islower():
    return ord(item) - ord('a') + 1
  else:
    return ord(item) - ord('A') + 27

priority_total = 0
for rucksack in inp:
  comp1, comp2 = get_compartments(rucksack)
  # print(comp1, comp2)
  shared_item = get_shared_item(comp1, comp2)
  priority = get_priority(shared_item)
  priority_total += priority

print(priority_total)
  

