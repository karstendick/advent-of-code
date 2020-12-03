grid = []


with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      grid.append(line)

# print(grid)

NROWS = len(grid)
NCOLS = len(grid[0])

# drow, dcol = 1, 3
product = 1

for drow, dcol in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
  trees_encountered = 0
  row, col = 0, 0
  while row < NROWS:
    location = grid[row][col]
    if location == '#':
      trees_encountered += 1
    row += drow
    col = (col + dcol) % NCOLS
  product *= trees_encountered

print(product)
