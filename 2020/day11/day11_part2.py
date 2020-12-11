from copy import deepcopy

with open('example2_input.txt', 'r') as f:
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
            while 0 < r and r < nrows and 0 < c and c < ncols:
                if grid[r][c] == 'L':
                    break
                if grid[r][c] == '#':
                    count += 1
                    break
                r += dr
                c += dc
            
    return count


def next_state(grid):
    next_grid = deepcopy(grid)
    nrows = len(next_grid)
    ncols = len(next_grid[0])

    neighbor_grid = [[-1]*ncols]*nrows

    for row in range(nrows):
        for col in range(ncols):
            cell = grid[row][col]
            num_neighbors = get_num_neighbors(grid, row, col, nrows, ncols)
            neighbor_grid[row][col] = num_neighbors
            if num_neighbors > 8:
                print('Invalid num_neighbors!!')
            if cell == '#' and num_neighbors >= 5:
                next_grid[row][col] = 'L'
            if cell == 'L' and num_neighbors == 0:
                next_grid[row][col] = '#'
    print(neighbor_grid)
    return next_grid

def print_grid(grid):
    for l in grid:
        print(''.join(l))
    print()

grid = lines
next_grid = next_state(grid)

while grid != next_grid:
    print_grid(grid)
    grid, next_grid = next_grid, next_state(next_grid)

answer = sum([l.count('#') for l in grid])
print(answer)

print_grid(grid)
