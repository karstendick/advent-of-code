from itertools import pairwise, product
import networkx as nx

inp = []
with open("example.txt", "r") as f:
    for line in f:
        inp.append(line.strip())

# print(inp)

num_keypad_edges = [
    ("7", "8", {"d": ">"}),
    ("7", "4", {"d": "v"}),
    ("8", "9", {"d": ">"}),
    ("8", "5", {"d": "v"}),
    ("8", "7", {"d": "<"}),
    ("9", "6", {"d": "v"}),
    ("9", "8", {"d": "<"}),
    ("4", "7", {"d": "^"}),
    ("4", "5", {"d": ">"}),
    ("4", "1", {"d": "v"}),
    ("5", "8", {"d": "^"}),
    ("5", "6", {"d": ">"}),
    ("5", "2", {"d": "v"}),
    ("5", "4", {"d": "<"}),
    ("6", "9", {"d": "^"}),
    ("6", "3", {"d": "v"}),
    ("6", "5", {"d": "<"}),
    ("1", "4", {"d": "^"}),
    ("1", "2", {"d": ">"}),
    ("2", "5", {"d": "^"}),
    ("2", "3", {"d": ">"}),
    ("2", "0", {"d": "v"}),
    ("2", "1", {"d": "<"}),
    ("3", "6", {"d": "^"}),
    ("3", "A", {"d": "v"}),
    ("3", "2", {"d": "<"}),
    ("0", "2", {"d": "^"}),
    ("0", "A", {"d": ">"}),
    ("A", "3", {"d": "^"}),
    ("A", "0", {"d": "<"}),
]
num_keypad_graph = nx.DiGraph(num_keypad_edges)
# print(num_keypad_graph)

dir_keypad_edges = [
    ("^", "A", {"d": ">"}),
    ("^", "v", {"d": "v"}),
    ("A", ">", {"d": "v"}),
    ("A", "^", {"d": "<"}),
    ("<", "v", {"d": ">"}),
    ("v", "^", {"d": "^"}),
    ("v", ">", {"d": ">"}),
    ("v", "<", {"d": "<"}),
    (">", "A", {"d": "^"}),
    (">", "v", {"d": "<"}),
]
dir_keypad_graph = nx.DiGraph(dir_keypad_edges)
# print(dir_keypad_graph)

# Keyed by the source node and then the target node
# e.g. num_paths["7"]["A"][0] == ['7', '8', '9', '6', '3', 'A']
num_paths = dict(nx.all_pairs_all_shortest_paths(num_keypad_graph))
dir_paths = dict(nx.all_pairs_all_shortest_paths(dir_keypad_graph))


def get_instruction_lists(code, graph, all_shortest_paths):
    arm = "A"
    instructions = []
    for c in code:
        path = all_shortest_paths[arm][c][0]
        path_edges = pairwise(path)
        for source, target in path_edges:
            instructions += graph[source][target]["d"]
        instructions += "A"
        arm = c
    return instructions


instructions = get_instruction_lists(inp[0], num_keypad_graph, num_paths)
print("".join(instructions), len(instructions))

instructions = get_instruction_lists(instructions, dir_keypad_graph, dir_paths)
print("".join(instructions), len(instructions))

instructions = get_instruction_lists(instructions, dir_keypad_graph, dir_paths)
print("".join(instructions), len(instructions))

code_int = int(inp[0][0:-1])
print(f'code_int: {code_int}')
len_seq = len(instructions)
print(f'len_seq: {len_seq}')
complexity = code_int * len_seq
print(complexity)
