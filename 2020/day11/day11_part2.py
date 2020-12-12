from copy import deepcopy

with open('input.txt', 'r') as f:
    lines = list(map(lambda l: l.strip(), f))

lines = [list(l) for l in lines]

def get_num_neighbors(grid, row, col, nrows, ncols):
    count = 0
    for dr in range(-1,2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            r = row + dr
            c = col + dc
            while 0 <= r and r < nrows and 0 <= c and c < ncols:
                if grid[r][c] == 'L':
                    break
                if grid[r][c] == '#':
                    # print(f"row,col: {row},{col} | dr,dc: {dr},{dc} | r,c: {r},{c} | grid: {grid[r][c]}")
                    count += 1
                    break
                r += dr
                c += dc
            
    return count


def next_state(grid):
    next_grid = deepcopy(grid)
    nrows = len(next_grid)
    ncols = len(next_grid[0])

    neighbor_grid = [[-1 for x in range(ncols)] for y in range(nrows)]

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
    # print_neighbors(neighbor_grid)
    return next_grid

def print_grid(grid):
    for l in grid:
        print(''.join(l))
    print()

def print_neighbors(neighbor_grid):
    # print(neighbor_grid)
    for row in neighbor_grid:
        row_strs = [str(x) for x in row]
        row_str = ''.join(row_strs)
        print(row_str)
    print()

grid = lines
# print_grid(grid)
next_grid = next_state(grid)

while grid != next_grid:
    # print_grid(next_grid)
    grid = deepcopy(next_grid)
    next_grid = next_state(next_grid)

answer = sum([l.count('#') for l in grid])
print(answer)

# print_grid(grid)

# import pdb; pdb.set_trace();

# get_num_neighbors(next_grid, 0, 13, len(next_grid), len(next_grid[0]))
# print(get_num_neighbors(next_grid, 0, 14, len(next_grid), len(next_grid[0])))
