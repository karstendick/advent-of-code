from anytree import Node, RenderTree

filename = 'input.txt'
# filename = 'example.txt'
with open(filename, 'r') as f:
    input_nodes = set()
    input_edges = []
    for line in f:
        line = line.rstrip('\n')
        parent, child = line.split(')')
        input_nodes.add(parent)
        input_nodes.add(child)
        input_edges.append((parent, child))

print(f'input_nodes: {input_nodes}')
print(f'input_edges: {input_edges}')

edge_dict = {child: parent for parent,child in input_edges}
nodes = [Node(input_node) for input_node in input_nodes]
node_dict = {node.name: node for node in nodes}

for node in nodes:
    if node.name != "COM":
        parent_string = edge_dict[node.name]
        node.parent = node_dict[parent_string]

root = node_dict["COM"]

# for pre, fill, node in RenderTree(root):
#     print("%s%s" % (pre, node.name))

total = 0
for node in nodes:
    total += len(node.ancestors)

print(f'total: {total}')
