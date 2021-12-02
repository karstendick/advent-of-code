nums = []

with open('input.txt', 'r') as f:
  for line in f:
    nums.append(int(line.strip()))

# print(nums)

increases = 0
last = nums[0]
for num in nums[1:]:
    if num > last:
        increases += 1
    last = num

print(increases)
