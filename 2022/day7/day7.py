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

root = Tree()
root.show()
pwd = root.create_node("/", data=Inode(0, 'dir')) # root node

# TODO:
# This approach of using the file/dir name for the treelib identifier
# does not work on the input, as the same file name can be used in different directories,
# i.e. relative path names are not unique.
# Global path names are unique, but it'll take some work to construct them and keep track of them :-(

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
      pwd = root.parent(pwd.identifier)
    else:
      print(f"cd to {dir}")
      pwd = [n for n in root.children(pwd.identifier) if n.tag == dir][0]
  elif mode == 'ls':
    size, name = line.split()
    if size == 'dir':
      node = root.create_node(name, data=Inode(0, 'dir'), parent=pwd.identifier)
      print(f"Adding dir {name} with identifer {node.identifier}")
    else:
      print(f"Adding file {name} with size {int(size)} in directory {pwd.identifier}")
      root.create_node(name, data=Inode(int(size), 'file'), parent=pwd.identifier)

root.show()
