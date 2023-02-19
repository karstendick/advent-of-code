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

def get_trees_seen(this_tree, trees):
  if not trees:
    return 0
  trees_seen = 0
  for tree in trees:
    trees_seen += 1
    if tree >= this_tree:
      break
  return trees_seen

def get_scenic_score(r, c):
  this_tree = grid[r][c]
  if r == 0 or c == 0 or r == NROWS-1 or c == NCOLS-1:
    return 0
  # from the left
  from_left = grid[r][:c]
  from_left = from_left[::-1]
  # from the right
  from_right = grid[r][c+1:]
  # from above
  from_above = [grid[row][c] for row in range(0,r)[::-1]]
  # from below
  from_below = [grid[row][c] for row in range(r+1,NROWS)]

  # print(f"from_left: {from_left}")
  # print(f"from_right: {from_right}")
  # print(f"from_above: {from_above}")
  # print(f"from_below: {from_below}")

  return get_trees_seen(this_tree, from_left) * \
         get_trees_seen(this_tree, from_right) * \
         get_trees_seen(this_tree, from_above) * \
         get_trees_seen(this_tree, from_below)

highest_score = 0
for r in range(NROWS):
  for c in range(NCOLS):
    score = get_scenic_score(r,c)
    if score > highest_score:
      highest_score = score

print(highest_score)

# print(f"should be 4: {get_scenic_score(1, 2)}")
# print(f"should be 8: {get_scenic_score(3, 2)}")
