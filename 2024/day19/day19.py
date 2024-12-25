import re

patterns, designs = [], []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if ',' in line:
            patterns = line.split(', ')
        elif line:
            designs.append(line)

# print(patterns)
# print(designs)

re_pattern = f'^({"|".join(patterns)})+$'
# print(re_pattern)
compiled_pattern = re.compile(re_pattern)

num_possible = 0
for design in designs:
    m = re.fullmatch(compiled_pattern, design)
    # print(m)
    if m:
        num_possible += 1

print(num_possible)
