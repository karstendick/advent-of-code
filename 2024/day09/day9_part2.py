from itertools import repeat

inp = []
with open('example.txt', 'r') as f:
  inp = [int(x) for x in f.read()]

# print(inp)
# print(len(inp))

def print_disk(disk):
  print(''.join([str(x) for x in disk]))

def swap(l, i, j):
  l[i], l[j] = l[j], l[i]

def compact(disk):
  compacted = []
  i, j = 0, len(disk) - 1
  while i < len(disk):
    e = disk[i]
    if e != '.':
      compacted.append(e)
    else:
      while disk[j] == '.':
        j -= 1
      if j <= i:
        break
      compacted.append(disk[j])
      swap(disk, i, j)
    i += 1

  return compacted

disk = []
id = 0
block_is_file = True
for block in inp:
  if block_is_file:
    # print(f'File: {block}')
    disk += repeat(id, block)
    id += 1
  else:
    # print(f'Free: {block}')
    disk += repeat('.', block)
  block_is_file = not block_is_file

# print_disk(disk)
compacted = compact(disk)
# print_disk(compacted)

checksum = 0
for i,e in enumerate(compacted):
  checksum += i*e

print(checksum)
