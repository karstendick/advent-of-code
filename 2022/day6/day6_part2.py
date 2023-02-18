import collections
from itertools import *

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())
inp = inp[0]

print(inp)

# From: https://docs.python.org/3/library/itertools.html
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def all_diff(s):
  return len(s) == len(set(s))

i = 0
for window in sliding_window(inp, 14):
  if all_diff(window):
    break
  i += 1

print(i+14)
