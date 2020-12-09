lines = []
with open('input.txt', 'r') as f:
    for line in f:
      line = line.strip()
      lines.append(int(line))

# target = 127
target = 258585477
for i in range(len(lines)):
    for j in range(i, len(lines)):
        subarray = lines[i:j+1]
        s = sum(subarray)
        if s == target:
            mmin = min(subarray)
            mmax = max(subarray)
            print(mmin + mmax)
