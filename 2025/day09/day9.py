inp = []
with open("input.txt", "r") as f:
    for line in f:
        inp.append([int(n) for n in line.strip().split(',')])

print(inp)

def calc_area(p1, p2):
    return (1+ abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))

largest_area = 0
for i in range(len(inp)):
    for j in range(i+1, len(inp)):
        area = calc_area(inp[i], inp[j])
        if area > largest_area:
            largest_area = area

print(largest_area)
