grid = []
with open("input.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

# print(grid)

def print_grid(grid):
    for row in grid:
        print(''.join(row))

num_rows = len(grid)
num_cols = len(grid[0])

# print(f'num_rows: {num_rows}, num_cols: {num_cols}')

num_splits = 0
for r in range(1, num_rows):
    for c in range(1, num_cols):
        if (grid[r - 1][c] == '|' or grid[r - 1][c] == 'S') and grid[r][c] == '.':
            # Start the beam or keep it going down
            grid[r][c] = '|'
    for c in range(1, num_cols):
        if grid[r][c] == '^' and grid[r - 1][c] == '|':
            # split the beam
            grid[r][c - 1] = '|'
            grid[r][c + 1] = '|'
            num_splits += 1


# print_grid(grid)
print(f'num_splits: {num_splits}')