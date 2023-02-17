nums = [[]]
i = 0
with open('input.txt', 'r') as f:
  for line in f:
    if line.strip():
        nums[i].append(int(line.strip()))
    else:
        nums.append([])
        i += 1

# print(nums)

elves = map(sum, nums)
print(sum(sorted(elves, reverse=True)[0:3]))
