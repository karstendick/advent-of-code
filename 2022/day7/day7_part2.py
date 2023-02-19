from treelib import Node, Tree

inp = []
with open('input.txt', 'r') as f:
  for line in f:
    inp.append(line.strip())

print(inp)

class Inode():
  def __init__(self, size, type) -> None:
    self.size = size
    self.type = type

tree = Tree()
tree.show()
root = tree.create_node("/", data=Inode(0, 'dir')) # root node

pwd = root
mode = None
for line in inp[1:]:
  if line == '$ ls':
    print("About to ls some files")
    if mode:
      raise Exception("How do you already have a mode?!")
    mode = 'ls'
  elif line.startswith('$ cd'):
    mode = None
    dir = line.split()[2]
    if dir == '..':
      print("cd up a directory")
      pwd = tree.parent(pwd.identifier)
    else:
      print(f"cd to {dir}")
      pwd = [n for n in tree.children(pwd.identifier) if n.tag == dir][0]
  elif mode == 'ls':
    size, name = line.split()
    if size == 'dir':
      node = tree.create_node(name, data=Inode(0, 'dir'), parent=pwd.identifier)
      print(f"Adding dir {name} with identifer {node.identifier}")
    else:
      print(f"Adding file {name} with size {int(size)} in directory {pwd.identifier}")
      tree.create_node(name, data=Inode(int(size), 'file'), parent=pwd.identifier)

tree.show()

def calc_dir_sizes(root):
  if root.data.type == 'dir':
    total_size = sum(map(lambda n: calc_dir_sizes(n), tree.children(root.identifier)))
    root.data.size = total_size
    return total_size
  else:
    return root.data.size

calc_dir_sizes(root)
total_size_used = root.data.size
size_unused = 70000000 - total_size_used
size_needed = 30000000 - size_unused

print (f"{total_size_used} is used, so {size_unused} is unused and {size_needed} is needed.")

tree.show(data_property="size")

nodes = tree.all_nodes()
dir_candidates = [n for n in nodes if n.data.type == 'dir' and n.data.size >= size_needed]
dir_candidate_sizes = map(lambda n: n.data.size, dir_candidates)
print(dir_candidates)
print(min(dir_candidate_sizes))
