inp = []
ranges = []
ids = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if '-' in line:
            ranges.append([int(x) for x in line.split('-')])
        elif line.strip().isdigit():
            ids.append(int(line.strip()))


# print(ranges)
# print(ids)

def is_valid(id):
    for r in ranges:
        if r[0] <= id and id <= r[1]:
            return True
    return False

valid_ids = []
for id in ids:
    if is_valid(id):
        valid_ids.append(id)

# print(valid_ids)
print(len(valid_ids))
