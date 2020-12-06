from functools import reduce

lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      lines.append(line)

def everyone_yes(c, ss):
    for s in ss:
        if c not in s:
            return False
    return True

counts = 0
s = set()
ss = []
all_c = set()
for i, line in enumerate(lines):
    if not line or i == len(lines) - 1:
        if i == len(lines) - 1:
            for c in line:
                s.add(c)
                all_c.add(c)
            ss.append(s)
        for c in all_c:
            if everyone_yes(c, ss):
                counts += 1
        s = set()
        ss = []
        all_c = set()
    else:
        for c in line:
            s.add(c)
            all_c.add(c)
        ss.append(s)
        s = set()

print(counts)
