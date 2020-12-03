grid = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      grid.append(line)

NROWS = len(grid)
NCOLS = len(grid[0])
trees_encountered = 0
row, col = 0, 0
drow, dcol = 1, 3

while row < NROWS:
  location = grid[row][col]
  if location == '#':
    trees_encountered += 1
  row += drow
  col = (col + dcol) % NCOLS

print(trees_encountered)
