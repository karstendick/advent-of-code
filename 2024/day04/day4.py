inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

# print(inp)
board = inp

def safe_get(board, r, c):
  if (0 <= r < len(board)) and (0 <= c < len(board[0])):
    return board[r][c]
  return ''

def string_at(board, r, c, dr, dc, n):
  s = ''
  ri = r
  ci = c
  for _ in range(n):
    s += safe_get(board, ri, ci)
    ri += dr
    ci += dc
  return s

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1], # N,E,S,W
      [-1, 1], [1, 1], [1, -1], [-1, -1] # NE,SE,SW,NW
      ]

cnt = 0
for r in range(len(board)):
  for c in range(len(board[0])):
    for dr, dc in dirs:
      s = string_at(board, r, c, dr, dc, 4)
      if s == 'XMAS':
        cnt += 1
        # print(f'({r}, {c})*[{dr}, {dc}]')

print(cnt)
