
nums = []

with open('input.txt', 'r') as f:
  for line in f:
    nums.append(int(line.strip()))

print(nums)

for x in nums:
  for y in nums:
    if x + y == 2020:
      print(f"Found it! (x,y)=({x},{y}). Product: {x*y}")

print("All done.")
