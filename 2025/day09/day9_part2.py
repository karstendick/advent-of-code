from shapely.geometry import Point, Polygon

red_tiles = []
with open("input.txt", "r") as f:
    for line in f:
        c, r = [int(n) for n in line.strip().split(",")]
        red_tiles.append((r, c))

polygon = Polygon(red_tiles)


def calc_area(p1, p2):
    return (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))


def get_rectangle_polygon(p1, p2):
    return Polygon([p1, (p1[0], p2[1]), p2, (p2[0], p1[1])])


largest_area = 0
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        rectangle = get_rectangle_polygon(red_tiles[i], red_tiles[j])
        if polygon.covers(rectangle):
            area = calc_area(red_tiles[i], red_tiles[j])
            if area > largest_area:
                largest_area = area

print(largest_area)
