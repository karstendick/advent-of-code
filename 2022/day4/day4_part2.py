inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(list(map(int, line.strip().translate(str.maketrans({'-': ' ', ',': ' '})).split())))

# print(inp)

def is_overlapping(start1, end1, start2, end2):
  return start2 <= end1 and end1 <= end2

count = 0
for start1, end1, start2, end2 in inp:
  if is_overlapping(start1, end1, start2, end2) or is_overlapping(start2, end2, start1, end1):
    print(start1, end1, start2, end2)
    count += 1

print(count)
