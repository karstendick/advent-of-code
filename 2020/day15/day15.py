# nums = [None, 0, 3, 6]  # example
nums = [None, 1, 12, 0, 20, 8, 16]  # input

def get_last_turn_spoken(last_num, index):
  while index >= 1:
    if nums[index] == last_num:
      return index
    index -= 1
  raise Exception("Oh no!")

i = len(nums) # turn number
while i <= 2020:
  last_num = nums[i - 1]
  if last_num in nums[1:i - 1]:
    last_turn_spoken = get_last_turn_spoken(last_num, i - 2)
    nums.append(i - 1 - last_turn_spoken)
  else:
    nums.append(0)
  i += 1

print(nums[-1])
