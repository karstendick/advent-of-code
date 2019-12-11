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
    points = set()
    pos = Point(0,0)
    for edge in edges:
        if edge.dir == 'U':
            for i in range(1, edge.len + 1):
                pos = Point(pos.x, pos.y+1)
                points.add(pos)
        elif edge.dir == 'D':
            for i in range(1, edge.len + 1):
                pos = Point(pos.x, pos.y-1)
                points.add(pos)
        elif edge.dir == 'R':
            for i in range(1, edge.len + 1):
                pos = Point(pos.x+1, pos.y)
                points.add(pos)
        elif edge.dir == 'L':
            for i in range(1, edge.len + 1):
                pos = Point(pos.x-1, pos.y)
                points.add(pos)
        else:
            raise ValueError(f'Unexpected direction: {edge.dir}. Expected one of: U,D,R,L.')
    return points

wire1_points = calc_points(wire1_edges)
wire2_points = calc_points(wire2_edges)
# print(f'wire1_points: {sorted(wire1_points)}')
# print(f'wire2_points: {sorted(wire2_points)}')

wire_crossings = wire1_points.intersection(wire2_points)
print(f'wire_crossings: {wire_crossings}')
dists = [abs(p.x) + abs(p.y) for p in wire_crossings]
print(f'Dist to closest intersection: {min(dists)}')
