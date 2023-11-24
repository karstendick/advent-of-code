import networkx as nx

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

starts = []
end = ''
elevation_map = []
for row, s in enumerate(inp):
  elevation_row = []
  for col, ch in enumerate(s):
    if ch == 'S':
      elevation = 0
      starts.append(f'r{row}c{col}')
    elif ch == 'E':
      elevation = 26
      end = f'r{row}c{col}'
    else:
      elevation = ord(ch) - ord('a')
      if elevation == 0:
        starts.append(f'r{row}c{col}')
    elevation_row.append(elevation)
  elevation_map.append(elevation_row)

# print(elevation_map)
# for row in elevation_map:
#   print(row)

def can_reach(start_row, start_col, end_row, end_col, elevation_map):
  start_elevation = elevation_map[start_row][start_col]
  end_elevation = elevation_map[end_row][end_col]
  if start_elevation >= end_elevation - 1:
    return True
  else:
    return False



edges = []
for row in range(len(elevation_map)):
  for col in range(len(elevation_map[0])):
    if (row > 0) and can_reach(row, col, row-1, col, elevation_map):
      edges.append((f'r{row}c{col}', f'r{row-1}c{col}', 1))
    if (row < len(elevation_map) - 1) and can_reach(row, col, row+1, col, elevation_map):
      edges.append((f'r{row}c{col}', f'r{row+1}c{col}', 1))
    if (col > 0) and can_reach(row, col, row, col-1, elevation_map):
      edges.append((f'r{row}c{col}', f'r{row}c{col-1}', 1))
    if (col < len(elevation_map[0]) - 1) and can_reach(row, col, row, col+1, elevation_map):
      edges.append((f'r{row}c{col}', f'r{row}c{col+1}', 1))
  
# print(edges)

G = nx.DiGraph()
G.add_weighted_edges_from(edges)

print(nx.multi_source_dijkstra(G, starts, end)[0])
