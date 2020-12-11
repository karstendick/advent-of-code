from copy import deepcopy

with open('input.txt', 'r') as f:
    lines = list(map(lambda l: l.strip(), f))

lines = [list(l) for l in lines]
print(lines)

def get_num_neighbors(grid, row, col, nrows, ncols):
    count = 0
    for dr in range(-1,2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            r = row + dr
            c = col + dc
            if r < 0 or r >= nrows or c < 0 or c >= ncols:
                continue
            if grid[r][c] == '#':
                count += 1
    return count


def next_state(grid):
    next_grid = deepcopy(grid)
    nrows = len(next_grid)
    ncols = len(next_grid[0])

    for row in range(nrows):
        for col in range(ncols):
            cell = grid[row][col]
            num_neighbors = get_num_neighbors(grid, row, col, nrows, ncols)
            if cell == '#' and num_neighbors >= 4:
                next_grid[row][col] = 'L'
            if cell == 'L' and num_neighbors == 0:
                next_grid[row][col] = '#'
    return next_grid

# def print_grid(grid):

grid = lines
next_grid = next_state(grid)

while grid != next_grid:

    grid, next_grid = next_grid, next_state(next_grid)

answer = sum([l.count('#') for l in grid])
print(answer)
