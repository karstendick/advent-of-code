import re

inp = []
with open('input.txt', 'r') as f:
  inp = f.read()

# print(inp)

matches = re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', inp)
# print(matches)

s = 0
enabled = True
for match in matches:
  num1, num2, do, dont = match
  if enabled and num1 and num2:
    s += int(num1)*int(num2)
  elif dont:
    enabled = False
  elif do:
    enabled = True

print(s)
