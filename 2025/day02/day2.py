inp = []
with open('input.txt', 'r') as f:
    line = f.readline()

ranges = line.split(',')
for r in ranges:
    start, end = r.split('-')
    inp.append((int(start), int(end)))

# print(inp)

def is_invalid(n):
    nstr = str(n)
    if len(nstr) % 2 != 0:
        return False
    return nstr[0:len(nstr)//2] == nstr[len(nstr)//2:]

invalid_id_sum = 0
for r in inp:
    start, end = r
    for i in range(start, end + 1):
        if is_invalid(i):
            invalid_id_sum += i

print(invalid_id_sum)
