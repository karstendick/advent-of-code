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
    return transformed_shapes

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

# print(shapes)
# print(regions)
for shape in shapes:
    transformed_shapes = get_transformed_shapes(shape)
    print(f"there are {len(transformed_shapes)} transformed shapes")
    for transformed_shape in transformed_shapes:
        print(transformed_shape)
        print_shape(transformed_shape)
        print()
    print("-"*20)

