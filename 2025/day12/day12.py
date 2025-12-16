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
with open("input.txt", "r") as f:
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

def has_valid_position(grid, num_rows, num_cols, shape_index):
    """Check if shape_index has at least one valid position on the grid."""
    for transformed_shape in all_transformed_shapes[shape_index]:
        for r in range(num_rows):
            for c in range(num_cols):
                if is_valid_position(grid, num_rows, num_cols, transformed_shape, r, c):
                    return True
    return False

# This approach was too slow.
def forward_check(grid, num_rows, num_cols, shape_counts):
    """Check that all remaining shapes have at least one valid position."""
    for shape_idx, count in enumerate(shape_counts):
        if count > 0:
            if not has_valid_position(grid, num_rows, num_cols, shape_idx):
                return False
    return True

def backtrack_search(region):
    (num_rows, num_cols), shape_counts = region

    # Quick area check: if shapes need more cells than grid has, impossible
    shape_size = len(shapes[0])  # all shapes have same size
    total_shape_cells = sum(shape_counts) * shape_size
    grid_area = num_rows * num_cols
    if total_shape_cells > grid_area:
        return False

    grid = [[False] * num_cols for _ in range(num_rows)]
    shape_counts = list(shape_counts)
    return backtrack(grid, num_rows, num_cols, shape_counts)

def backtrack(grid, num_rows, num_cols, shape_counts):
    if all(c == 0 for c in shape_counts):
        return True  # All shapes placed successfully

    # Find the first shape type we still need to place
    shape_index = None
    for i, count in enumerate(shape_counts):
        if count > 0:
            shape_index = i
            break

    # Try all transformed versions of this shape
    for transformed_shape in all_transformed_shapes[shape_index]:
        for r in range(num_rows):
            for c in range(num_cols):
                if is_valid_position(grid, num_rows, num_cols, transformed_shape, r, c):
                    assign(grid, transformed_shape, r, c, True)
                    shape_counts[shape_index] -= 1

                    if backtrack(grid, num_rows, num_cols, shape_counts):
                        return True

                    assign(grid, transformed_shape, r, c, False)
                    shape_counts[shape_index] += 1

    return False

total = 0
for i, region in enumerate(regions):
    result = backtrack_search(region)
    print(f"region #{i}: {region} -> {result}")
    if result:
        total += 1
print(total)
