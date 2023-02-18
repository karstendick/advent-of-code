inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(list(map(int, line.strip().translate(str.maketrans({'-': ' ', ',': ' '})).split())))
    #.translate(str.maketrans({'-': ' ', ',': ' '})).split()

# print(inp)

def is_within(start1, end1, start2, end2):
  return start1 <= start2 and end2 <= end1

count = 0
for start1, end1, start2, end2 in inp:
  if is_within(start1, end1, start2, end2) or is_within(start2, end2, start1, end1):
    count += 1

print(count)
  

