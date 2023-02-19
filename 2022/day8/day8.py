inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

grid = []
for line in inp:
  grid.append(list(map(int, line)))

print(grid)
NROWS = len(grid)
NCOLS = len(grid[0])

def is_visible(r, c):
  this_tree = grid[r][c]
  if r == 0 or c == 0 or r == NROWS-1 or c == NCOLS-1:
    return True
  # from the left
  others = grid[r][:c]
  if this_tree > max(others):
    return True
  # from the right
  others = grid[r][c+1:]
  if this_tree > max(others):
    return True
  # from above
  others = [grid[row][c] for row in range(0,r)]
  if this_tree > max(others):
    return True
  # from below
  others = [grid[row][c] for row in range(r+1,NROWS)]
  if this_tree > max(others):
    return True
  return False

num_visible = 0
for r in range(NROWS):
  for c in range(NCOLS):
    if is_visible(r,c):
      num_visible += 1
      # print(f"[{r},{c}] is visible")
    else:
      pass
      # print(f"[{r},{c}] is NOT visible")

print(num_visible)
