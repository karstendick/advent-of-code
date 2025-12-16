from collections import deque

def parse_region(line):
    cxr_str, indexes_str = line.split(":")
    c, r = [int(n) for n in cxr_str.split("x")]
    indexes = tuple([int(n) for n in indexes_str.split(" ") if n != ""])
    return ((r, c), indexes)


def parse_shape(shape_strs):
    num_rows = len(shape_strs)
    num_cols = len(shape_strs[0])
    shape = []
    for r in range(num_rows):
        for c in range(num_cols):
            if shape_strs[r][c] == "#":
                shape.append((r, c))
    return frozenset(shape)


def print_shape(shape):
    num_rows = max(r for r, c in shape) + 1
    num_cols = max(c for r, c in shape) + 1
    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) in shape:
                print("#", end="")
            else:
                print(".", end="")
        print()

def rotate_shape_once(shape):
    max_row = max(r for r, c in shape)
    rotated_shape = [(c, -r + max_row) for r, c in shape]
    return frozenset(rotated_shape)

def rotate_shape(shape, times):
    rotated_shape = shape
    for _ in range(times):
        rotated_shape = rotate_shape_once(rotated_shape)
    return rotated_shape

def flip_shape(shape):
    max_row = max(r for r, c in shape)
    flipped_shape = [(max_row - r, c) for r, c in shape]
    return frozenset(flipped_shape)
    
def get_transformed_shapes(shape):
    rotated_shapes = frozenset([rotate_shape(shape, i) for i in range(4)])
    flipped_shape = flip_shape(shape)
    rotated_flipped_shapes = frozenset([rotate_shape(flipped_shape, i) for i in range(4)])
    transformed_shapes = rotated_shapes | rotated_flipped_shapes
    return tuple(list(transformed_shapes))

shapes = []
regions = []
with open("example.txt", "r") as f:
    shape_strs = []
    for line in f:
        line = line.strip()
        if "x" in line:
            region = parse_region(line)
            regions.append(region)
        elif "#" in line:
            shape_strs.append(line)
        else:
            if shape_strs != []:
                shapes.append(parse_shape(shape_strs))
                shape_strs = []

shapes = tuple(shapes)
regions = tuple(regions)
# print(shapes)
# print(regions)
all_transformed_shapes = []
for shape in shapes:
    transformed_shapes = get_transformed_shapes(shape)
    all_transformed_shapes.append(transformed_shapes)
    # print(f"there are {len(transformed_shapes)} transformed shapes")
    # for transformed_shape in transformed_shapes:
    #     print(transformed_shape)
    #     print_shape(transformed_shape)
    #     print()
    # print("-"*20)

all_transformed_shapes = tuple(all_transformed_shapes)

# print(all_transformed_shapes)

# csp
# grid (list of lists of booleans)
# grid[r][c] = False if empty, True if shape
# regions is tuples of (num_rows, num_cols, list of shape indices)
# Inputs include:
# num_rows, num_cols
# list of shape counts -- When this is all zeroes, the problem is solved
# current shape index
# current transformed shape index

# assignment
# deque of tuples (shape_index, transformed_shape_index, (r, c))
# each tuple represents a shape being placed in a region
# the shape is represented by its index in `shapes`
# the transformed shape is represented by its index in the transformed shapes tuple
# the position is represented by a tuple (r, c)
# the position is the top left corner of the transformed shape in the region

def is_complete(shape_counts):
    return all(count == 0 for count in shape_counts)

def is_valid_position(grid, num_rows, num_cols, transformed_shape, r, c):
    for (tr, tc) in transformed_shape:
        if not (0 <= r + tr < num_rows) or not (0 <= c + tc < num_cols):
            return False
        if grid[r + tr][c + tc]:
            return False
    return True

def assign(grid, transformed_shape, r, c, value):
    for (tr, tc) in transformed_shape:
        grid[r + tr][c + tc] = value

def get_next_assignments(grid, num_rows, num_cols, shape_counts, shape_index_min, transformed_shape_index_min, r_min, c_min):
    if shape_counts[shape_index_min] > 0:
        yield from get_next_assignment_for_shape(grid, num_rows, num_cols, shape_index_min, transformed_shape_index_min, r_min, c_min)
    for shape_index in range(shape_index_min + 1, len(shapes)):
        if shape_counts[shape_index] > 0:
            yield from get_next_assignment_for_shape(grid, num_rows, num_cols, shape_index, 0, 0, 0)
    return None

def get_next_assignment_for_shape(grid, num_rows, num_cols, shape_index, transformed_shape_index_min, r_min, c_min):
    for transformed_shape_index in range(transformed_shape_index_min, len(all_transformed_shapes[shape_index])):
        transformed_shape = all_transformed_shapes[shape_index][transformed_shape_index]
        for r in range(r_min, num_rows):
            for c in range(c_min + 1, num_cols):
                if is_valid_position(grid, num_rows, num_cols, transformed_shape, r, c):
                    yield (shape_index, transformed_shape_index, (r, c))

def is_shape_index_min_valid(shape_counts, shape_index_min):
    for shape_index in range(0, shape_index_min):
        if shape_counts[shape_index] > 0:
            return False
    return True

def backtrack_search(region):
    (num_rows, num_cols), shape_counts = region
    shape_counts = list(shape_counts)
    grid = [[False] * num_cols for _ in range(num_rows)]
    assignment = deque()
    return backtrack(grid, num_rows, num_cols, shape_counts, 0, 0, 0, 0, assignment)

def backtrack(grid, num_rows, num_cols, shape_counts, shape_index_min, transformed_shape_index_min, r_min, c_min, assignment):
    # print(f"shape_counts: {shape_counts}, shape_index_min: {shape_index_min}, transformed_shape_index_min: {transformed_shape_index_min}, r_min: {r_min}, c_min: {c_min}")
    if is_complete(shape_counts):
        return assignment
    for next_assignment in get_next_assignments(grid, num_rows, num_cols, shape_counts, shape_index_min, transformed_shape_index_min, r_min, c_min):
        # if next_assignment is None:
        #     return None
        shape_index, transformed_shape_index, (r, c) = next_assignment
        # if not is_shape_index_min_valid(shape_counts, shape_index):
        #     return None
        transformed_shape = all_transformed_shapes[shape_index][transformed_shape_index]
        assign(grid, transformed_shape, r, c, True)
        shape_counts[shape_index] -= 1
        assignment.append((shape_index, transformed_shape_index, (r, c)))
        result = backtrack(grid, num_rows, num_cols, shape_counts, shape_index, transformed_shape_index, r, c, assignment)
        if result is not None:
            return result
        # backtrack!
        assign(grid, transformed_shape, r, c, False)
        shape_counts[shape_index] += 1
        assignment.pop()
    return None

total = 0
for i, region in enumerate(regions):
    assignment = backtrack_search(region)
    print(f"region #{i}: {region}")
    print(f"assignment #{i}: {assignment}")
    print()
    if assignment is not None:
        total += 1
print(total)
