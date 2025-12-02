inp = []
with open('input.txt', 'r') as f:
    line = f.readline()

ranges = line.split(',')
for r in ranges:
    start, end = r.split('-')
    inp.append((int(start), int(end)))

# print(inp)

def is_repeating(nstr, k):
    ntimes = len(nstr) // k
    for j in range(1, ntimes):
        # print(f'Comparing {nstr[0:k]} and {nstr[j*k:(j+1)*k]}')
        if nstr[0:k] != nstr[j*k:(j+1)*k]:
            return False
    return True

# print(is_repeating('11111', 1))
# print(is_repeating('1212', 2))
# print(is_repeating('123123', 3))
# print(is_repeating('123123', 4))

# print(is_repeating('11', 1))
# print(is_repeating('22', 1))
# print(is_repeating('99', 1))
# print(is_repeating('111', 1))
# print(is_repeating('999', 1))
# print(is_repeating('1010', 2))
# print(is_repeating('1188511885', 5))

# print(is_repeating('100', 1))
# print(is_repeating('100', 2))
# print(is_repeating('100', 3))

def is_invalid(n):
    nstr = str(n)
    for i in range(1, len(nstr)//2 + 1):
        if len(nstr) % i != 0:
            continue
        if is_repeating(nstr, i):
            return True
    return False

invalid_id_sum = 0
for r in inp:
    start, end = r
    for i in range(start, end + 1):
        if is_invalid(i):
            # print(f'Invalid ID: {i}')
            invalid_id_sum += i

print(invalid_id_sum)
