from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Edge = namedtuple('Edge', ['dir', 'len'])

# filename = 'example.txt'
filename = 'input.txt'
with open(filename, 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

wire1_str = lines[0]
wire2_str = lines[1]

wire1_edges = [Edge(s[0], int(s[1:])) for s in wire1_str.split(',')]
wire2_edges = [Edge(s[0], int(s[1:])) for s in wire2_str.split(',')]

# print(f'wire1_edges: {wire1_edges}')
# print(f'wire2_edges: {wire2_edges}')

def calc_points(edges):
    points_map = {}
    pos = Point(0,0)
    path_len = 0
    for edge in edges:
        if edge.dir == 'U':
            for i in range(1, edge.len + 1):
                pos = Point(pos.x, pos.y+1)
                path_len += 1
                if pos not in points_map:
                    points_map[pos] = path_len
        elif edge.dir == 'D':
            for i in range(1, edge.len + 1):
                pos = Point(pos.x, pos.y-1)
                path_len += 1
                if pos not in points_map:
                    points_map[pos] = path_len
        elif edge.dir == 'R':
            for i in range(1, edge.len + 1):
                pos = Point(pos.x+1, pos.y)
                path_len += 1
                if pos not in points_map:
                    points_map[pos] = path_len
        elif edge.dir == 'L':
            for i in range(1, edge.len + 1):
                pos = Point(pos.x-1, pos.y)
                path_len += 1
                if pos not in points_map:
                    points_map[pos] = path_len
        else:
            raise ValueError(f'Unexpected direction: {edge.dir}. Expected one of: U,D,R,L.')
    return points_map

wire1_points_map = calc_points(wire1_edges)
wire2_points_map = calc_points(wire2_edges)
# print(f'wire1_points_map: {sorted(wire1_points_map)}')
# print(f'wire2_points_map: {sorted(wire2_points_map)}')

wire_crossings = wire1_points_map.keys() & wire2_points_map.keys()
print(f'wire_crossings: {wire_crossings}')
dists = [wire1_points_map[p] + wire2_points_map[p] for p in wire_crossings]
print(f'Dist to closest intersection: {min(dists)}')
