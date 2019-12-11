MIN = 246540
MAX = 787419

def has_double(nstr):
    nstr = 'ab' + nstr + 'xy'
    for i in range(2,7):
        if nstr[i] == nstr[i+1] and \
            nstr[i] != nstr[i+2] and \
            nstr[i] != nstr[i-1]:
            return True
    return False

def is_non_decr(nstr):
    for i in range(1,6):
        if nstr[i] < nstr[i-1]:
            return False
    return True

def is_cand(n):
    nstr = str(n)
    return has_double(nstr) and is_non_decr(nstr)

count = 0
for i in range(MIN, MAX+1):
    if is_cand(i):
        count += 1

print(f'count: {count}')

import pdb; pdb.set_trace();
