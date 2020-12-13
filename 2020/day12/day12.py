with open('input.txt', 'r') as f:
    lines = list(map(lambda l: l.strip(), f))

lines = [(l[0], int(l[1:])) for l in lines]

# print(lines)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

degrees_to_index = {90: 1, 180: 2, 270: 3}

def move_one(inst, x, y, dirx, diry, diri):
    op, num = inst
    if op == 'N':
        y += num
    if op == 'S':
        y -= num
    if op == 'E':
        x += num
    if op == 'W':
        x -= num
    if op == 'F':
        x += dirx * num
        y += diry * num
    if op == 'R':
        diri = (diri + degrees_to_index[num]) % 4
        if diri not in range(4):
            print(f"({x}, {y}) | ({dirx}, {diry}) | {diri}")
        dirx, diry = dirs[diri]
    if op == 'L':
        diri = (diri - degrees_to_index[num]) % 4
        if diri not in range(4):
            print(f"({x}, {y}) | ({dirx}, {diry}) | {diri}")
        dirx, diry = dirs[diri]
    return x, y, dirx, diry, diri


x, y = 0, 0
dirx, diry = 1, 0
diri = 1

for line in lines:
    # print(line)
    x, y, dirx, diry, diri = move_one(line, x, y, dirx, diry, diri)
    # print(f"({x}, {y}) | ({dirx}, {diry}) | {diri}")

print(f"{abs(x)+abs(y)} | ({x},{y})")
