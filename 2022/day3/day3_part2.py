from itertools import *

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())


# print(inp)

# From: https://docs.python.org/3/library/itertools.html
def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

def get_shared_item(e1, e2, e3):
  return set(e1).intersection(set(e2), set(e3)).pop()

def get_priority(item):
  if item.islower():
    return ord(item) - ord('a') + 1
  else:
    return ord(item) - ord('A') + 27

groups = list(grouper(inp, 3))
# print(groups)

priority_total = 0
for e1, e2, e3 in groups:
  # print(comp1, comp2)
  shared_item = get_shared_item(e1, e2, e3)
  priority = get_priority(shared_item)
  priority_total += priority

print(priority_total)
