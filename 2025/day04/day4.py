inp = []
with open("input.txt", "r") as f:
    for line in f:
        inp.append(line.strip())

# print(inp)

nrows = len(inp)
ncols = len(inp[0])


def get_cell(r, c):
    if 0 <= r < nrows and 0 <= c < ncols:
        return inp[r][c]
    return None


def get_neighbors(r, c):
    neighbors = []
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            rr = r + dr
            cc = c + dc
            cell = get_cell(rr, cc)
            if cell:
                neighbors.append(cell)
    return neighbors


total = 0
for r in range(nrows):
    for c in range(ncols):
        if get_cell(r, c) != "@":
            continue
        neighbors = get_neighbors(r, c)
        adj_rolls_count = 0
        for neighbor in neighbors:
            if neighbor == "@":
                adj_rolls_count += 1
        if adj_rolls_count < 4:
            # print(f'({r}, {c}) has {adj_rolls_count} adjacent rolls')
            total += 1
print(total)
