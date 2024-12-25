from functools import cache

patterns, designs = [], []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "," in line:
            patterns = line.split(", ")
        elif line:
            designs.append(line)

# print(patterns)
# print(designs)


@cache
def num_matches(design):
    if not design:
        return 1
    total = 0
    for p in patterns:
        if design.startswith(p):
            total += num_matches(design[len(p) :])
    return total


match_nums = [num_matches(design) for design in designs]
# print(match_nums)
print(sum(match_nums))
