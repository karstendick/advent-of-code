inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

board = inp

def safe_get(board, r, c):
  if (0 <= r < len(board)) and (0 <= c < len(board[0])):
    return board[r][c]
  return ''

def is_xmas(board, r, c):
  sw_to_ne = set([safe_get(board, r+1, c-1), safe_get(board, r-1, c+1)])
  nw_to_se = set([safe_get(board, r-1, c-1), safe_get(board, r+1, c+1)])
  return sw_to_ne == set('MS') and nw_to_se == set('MS')

cnt = 0
for r in range(len(board)):
  for c in range(len(board[0])):
    e = safe_get(board, r, c)
    if e == 'A' and is_xmas(board, r, c):
      cnt += 1

print(cnt)
