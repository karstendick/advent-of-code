ranges = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "-" in line:
            ranges.append([int(x) for x in line.split("-")])

def is_disjoint(r1, r2):
    r1_start, r1_end = r1
    r2_start, r2_end = r2
    return r1_end < r2_start or r2_end < r1_start


def merge_ranges(r1, r2):
    r1_start, r1_end = r1
    r2_start, r2_end = r2
    return [min(r1_start, r2_start), max(r1_end, r2_end)]

def get_disjoint_ranges(ranges):
    disjoint_ranges = []
    disjoint_ranges.append(ranges[0])
    for r in ranges[1:]:
        r_is_disjoint = True
        for dr in disjoint_ranges:
            if is_disjoint(r, dr):
                continue
            else:
                r_is_disjoint = False
                merged_range = merge_ranges(r, dr)
                disjoint_ranges.remove(dr)
                disjoint_ranges.append(merged_range)
        if r_is_disjoint:
            disjoint_ranges.append(r)
    return disjoint_ranges

num_ranges = len(ranges)
while True:
    ranges = get_disjoint_ranges(ranges)
    if len(ranges) == num_ranges:
        break
    num_ranges = len(ranges)

# print(ranges)

total = 0
for r in ranges:
    total += r[1] - r[0] + 1

print(total)
