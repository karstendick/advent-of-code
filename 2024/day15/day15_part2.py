from collections import deque
from operator import itemgetter

warehouse = []
moves = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            line = (
                line.replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )
            warehouse.append(list(line))
        elif line and line[0] in "<>^v":
            moves.extend(line)


def print_warehouse():
    for row in warehouse:
        print("".join(row))


# print(warehouse)
# print("Starting warehouse:")
# print_warehouse()
# print(moves)


def find_index_2d(array, value):
    for r, row in enumerate(array):
        if value in row:
            return (r, row.index(value))
    return None


def swap(fromr, fromc, tor, toc):
    warehouse[fromr][fromc], warehouse[tor][toc] = (
        warehouse[tor][toc],
        warehouse[fromr][fromc],
    )


def move_cell(rc, dr, dc):
    r, c = rc
    targetr, targetc = r + dr, c + dc
    swap(r, c, targetr, targetc)


def get_cell(rc):
    r, c = rc
    return warehouse[r][c]


robotr, robotc = find_index_2d(warehouse, "@")
# print(f'({robotr}, {robotc})')


def get_neighbors(rc, dr, dc):
    r, c = rc
    targetr, targetc = r + dr, c + dc
    value = warehouse[targetr][targetc]
    if value == "#":  # Hit a wall
        return None
    elif value == ".":
        return []
    elif value == "[":
        return [(targetr, targetc), (targetr, targetc + 1)]
    elif value == "]":
        return [(targetr, targetc - 1), (targetr, targetc)]
    else:
        raise Exception(f'Unexpected value {value} at {rc} in get_neighbors')


def get_boxes_to_move(first_box, dr, dc):
    boxes = []
    visited = set()
    queue = deque(first_box)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            boxes.append(node)
            neighbors = get_neighbors(node, dr, dc)
            if neighbors == None:
                return None
            unvisited_neighbors = [n for n in neighbors if n not in visited]
            queue.extend(unvisited_neighbors)
    return boxes

def sort_boxes_to_move(boxes, move):
    if move == '^':
        return sorted(boxes, key=itemgetter(0, 1), reverse=False)
    elif move == 'v':
        return sorted(boxes, key=itemgetter(0, 1), reverse=True)
    elif move == '>':
        return sorted(boxes, key=itemgetter(1, 0), reverse=True)
    elif move == '<':
        return sorted(boxes, key=itemgetter(1, 0), reverse=False)

# NESW vectors
vs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def move_one(move):
    global robotr, robotc
    (dr, dc) = vs[move]
    targetr, targetc = robotr + dr, robotc + dc
    target_val = warehouse[targetr][targetc]
    if target_val == ".":  # empty space
        swap(robotr, robotc, targetr, targetc)
        robotr, robotc = targetr, targetc
        return
    elif target_val == "#":  # wall
        return
    elif target_val in "[]":
        if target_val == "[":
            first_box = [(targetr, targetc), (targetr, targetc + 1)]
        else:
            first_box = [(targetr, targetc - 1), (targetr, targetc)]
        boxes_to_move = get_boxes_to_move(first_box, dr, dc)
        if boxes_to_move == None:  # Hit a wall
            return
        boxes_to_move = sort_boxes_to_move(boxes_to_move, move)
        # print(f"About to move {move}: {boxes_to_move}")
        for box in boxes_to_move:
            move_cell(box, dr, dc)
        swap(robotr, robotc, targetr, targetc)
        robotr, robotc = targetr, targetc
        return
    else:
        raise Exception(f"Unknown target value {target_val} at ({targetr}, {targetc})")


for i, move in enumerate(moves):
    # print(f"Move #{i}: {move}")
    move_one(move)
    # print_warehouse()

total = 0
for r, row in enumerate(warehouse):
    for c, e in enumerate(row):
        if e == "[":  # TODO: Change to []
            total += 100 * r + c

print(total)
