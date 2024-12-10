from itertools import repeat
from copy import deepcopy

inp = []
with open('input.txt', 'r') as f:
  inp = [int(x) for x in f.read()]


def print_disk(disk):
  print(''.join([str(x) for x in disk]))

def swap(l, i, j):
  l[i], l[j] = l[j], l[i]

def swap_range(l, imin, jmin, n):
  for i in range(n):
    swap(l, imin+i, jmin+i)

# Returns the index of the beginning of
# the first n contiguous blocks of free space;
# or None if none exists
# N.B. Pass this a slice of the disk, not the whole thing,
# or else you'll try to swap things to the right
def find_free(l, n):
  i = 0
  while i < len(l):
    while i < len(l) and l[i] != '.':
      i += 1
    if i >= len(l):
      break
    if i+n <= len(l) and l[i:i+n] == list('.'*n):
      return i
    i += 1
  return None

def compact(disk):
  compacted = deepcopy(disk)
  j = len(compacted) - 1
  while j > 0:
    while compacted[j] == '.':
      j -= 1
    if j <= 0:
      break
    id = compacted[j]
    jmin = j
    while compacted[jmin] == id:
      jmin -= 1
    jmin += 1
    # print(f'Found ID {id}: [{jmin}, {j}]')
    # want to swap the file in jmin to j (inclusive)
    # find the first free space large enough to fit this
    n = j - jmin + 1
    i = find_free(compacted[0:jmin], n)
    if i:
      # print(f'Swapping ID {id} from {jmin} to {i} ({n} blocks)')
      swap_range(compacted, i, jmin, n)
    else:
      # print(f'Could not find a place to put ID {id}')
      pass
    j = jmin - 1

  return compacted

disk = []
id = 0
block_is_file = True
for block in inp:
  if block_is_file:
    disk += repeat(id, block)
    id += 1
  else:
    disk += repeat('.', block)
  block_is_file = not block_is_file

# print_disk(disk)
compacted = compact(disk)
# print_disk(compacted)

checksum = 0
for i,e in enumerate(compacted):
  if e != '.':
    checksum += i*e

print(checksum)
