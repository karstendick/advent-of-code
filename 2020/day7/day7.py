from collections import defaultdict

lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip().rstrip('.')
      lines.append(line)

inner_to_outers = defaultdict(list)
for line in lines:
  outer_bag, inner_bags_str = line.split(' bags contain ')
  inner_bags_list = inner_bags_str.split(', ')
  inner_bags = [f"{s.split(' ') [1]} {s.split(' ') [2]}" for s in inner_bags_list]
  if inner_bags == ['other bags']:
    inner_bags = []
  else:
    for inner_bag in inner_bags:
      inner_to_outers[inner_bag].append(outer_bag)
  # print(f"{outer_bag} | {inner_bags}")

# print(inner_to_outers)

node = 'shiny gold'

def bfs(graph, node):
  visited = [node]
  queue = [node]

  while queue:
    s = queue.pop(0)

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return visited

visited = bfs(inner_to_outers, node)
print(len(set(visited))-1) # Don't count shiny gold
