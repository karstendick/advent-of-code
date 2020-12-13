import operator
from functools import reduce

with open('input.txt', 'r') as f:
    _ = f.readline()
    bus_ids = [(b[0],int(b[1])) for b in enumerate(f.readline().strip().split(',')) if b[1] != 'x']


print(bus_ids)

def prod(l):
    return reduce(operator.mul, l, 1)

def inverse(a, n):
    t = 0
    r = n
    newt = 1
    newr = a

    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    
    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t += n
    return t


# print(inverse(7, 31))

M = prod([b[1] for b in bus_ids])
t = 0
for a, m in bus_ids:
    b = M // m
    binv = inverse(b, m)
    t += (-a * b * binv) % M
    print(f"x = -{a} mod {m} | b: {b} | binv: {binv} | t: {t}")

print(f"t: {t}")
print(f"M: {M}")
print(t % M)
