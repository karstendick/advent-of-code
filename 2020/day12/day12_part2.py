from math import sin, cos, radians

with open('input.txt', 'r') as f:
    lines = list(map(lambda l: l.strip(), f))

lines = [(l[0], int(l[1:])) for l in lines]

def rotate_right(x, y, angle_degrees):
    cos_theta = int(cos(radians(angle_degrees)))
    sin_theta = int(sin(radians(angle_degrees)))
    xrot = x * cos_theta + y * sin_theta
    yrot = -x * sin_theta + y * cos_theta
    return xrot, yrot

def move_one(inst, x, y, shipx, shipy):
    op, num = inst
    if op == 'N':
        y += num
    if op == 'S':
        y -= num
    if op == 'E':
        x += num
    if op == 'W':
        x -= num
    if op == 'F':
        shipx += x * num
        shipy += y * num
    if op == 'R':
        x, y = rotate_right(x, y, num)
    if op == 'L':
        x, y = rotate_right(x, y, -1 * num)
    return x, y, shipx, shipy


x, y = 10, 1
shipx, shipy = 0, 0

for line in lines:
    # print(line)
    x, y, shipx, shipy = move_one(line, x, y, shipx, shipy)
    # print(f"({x}, {y}) | ({dirx}, {diry}) | {diri}")

print(f"{abs(shipx)+abs(shipy)} | ({shipx},{shipy})")
