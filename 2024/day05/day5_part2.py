from collections import defaultdict, deque

before_to_after = defaultdict(set)
after_to_before = defaultdict(set)
updates = []
with open('input.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if '|' in line:
      before, after = [int(x) for x in line.split('|')]
      before_to_after[before].add(after)
      after_to_before[after].add(before)
    elif ',' in line:
      update = [int(x) for x in line.split(',')]
      updates.append(update)

# print(before_to_after)
# print(after_to_before)
# print(updates)

def is_ordered(update):
  for i, page in enumerate(update):
    befores = set(update[0:i])
    afters = set(update[i+1:])
    if not afters.isdisjoint(after_to_before[page]):
      return False
    # I think this check is redundant:
    if not befores.isdisjoint(before_to_after[page]):
      return False
  return True

def get_ordered_update(update):
  graph = {key: {val for val in before_to_after[key] if val in update}
           for key in before_to_after if key in update}
  # print(graph)
  indegree = defaultdict(int)
  for node in graph:
    for neighbor in graph[node]:
      indegree[neighbor] += 1
  
  queue = deque([node for node in graph if indegree[node] == 0])
  sorted_order = []

  while queue:
    node = queue.popleft()
    sorted_order.append(node)

    for neighbor in graph[node]:
      indegree[neighbor] -= 1
      if indegree[neighbor] == 0:
        queue.append(neighbor)

  return sorted_order

total = 0
for update in updates:
  if not is_ordered(update):
    ordered_update = get_ordered_update(update)
    middle_page_num = ordered_update[len(ordered_update) // 2]
    total += middle_page_num

print(total)
