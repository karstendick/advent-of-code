# nums = [-1, 0, 3, 6]  # example
nums = [-1, 1, 12, 0, 20, 8, 16]  # input

last_turns_spoken = {e: i for i,e in enumerate(nums)}
i = len(nums)  # turn number
new_num = None
while i <= 30000000:
  last_num = nums[i - 1]
  # print(f"{last_num} | {i} | {last_turns_spoken}")
  if last_num in last_turns_spoken:
    last_turn_spoken = last_turns_spoken[last_num]
    new_num = i - 1 - last_turn_spoken
  else:
    new_num = 0
  # print(f"new_num: {new_num}")
  nums.append(new_num)
  last_turns_spoken[last_num] = i - 1
  i += 1

print(nums[-1])
# print(nums)
