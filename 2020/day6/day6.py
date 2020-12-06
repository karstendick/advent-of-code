lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      lines.append(line)

counts = 0
s = set()
for i, line in enumerate(lines):
    if not line or i == len(lines) - 1:
        if i == len(lines) - 1:
            for c in line:
                s.add(c)
        print(f"s: {s}")
        counts += len(s)
        s = set()
    for c in line:
        s.add(c)

print(counts)
