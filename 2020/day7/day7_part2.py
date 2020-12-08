lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip().rstrip('.')
      lines.append(line)

outer_to_inners = {}
for line in lines:
  outer_bag, inner_bags_str = line.split(' bags contain ')
  inner_bags_list = inner_bags_str.split(', ')
  for inner_bag in inner_bags_list:
    if inner_bag == 'no other bags':
      outer_to_inners[outer_bag] = []
    else:
      inner_bags = [(int(s.split(' ')[0]), f"{s.split(' ') [1]} {s.split(' ') [2]}") for s in inner_bags_list]
      outer_to_inners[outer_bag] = inner_bags

def num_bags_inside(outer_to_inners, outer_bag):
  inner_bags = outer_to_inners[outer_bag]
  total = 0
  for num, inner_bag in inner_bags:
    total += num + num * num_bags_inside(outer_to_inners, inner_bag)
  return total

print(num_bags_inside(outer_to_inners, 'shiny gold'))
