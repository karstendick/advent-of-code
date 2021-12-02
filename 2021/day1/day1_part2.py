nums = []

with open('input.txt', 'r') as f:
  for line in f:
    nums.append(int(line.strip()))

# print(nums)

increases = 0
last = nums[0]
for i, num in enumerate(nums[3:]):
    last_window = sum(nums[i:i+3])
    this_window = sum(nums[i+1:i+4])
    # print(f'{last_window}, {this_window}')
    if this_window > last_window:
        increases += 1

print(increases)
