import re

inp = []
with open('input.txt', 'r') as f:
  inp = f.read()

# print(inp)

matches = re.findall(r'mul\((\d+),(\d+)\)', inp)
# print(matches)

s = 0
for match in matches:
  s += int(match[0])*int(match[1])

print(s)
