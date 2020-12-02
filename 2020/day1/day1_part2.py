
nums = []

with open('input.txt', 'r') as f:
  for line in f:
    nums.append(int(line.strip()))

print(len(nums))

for x in nums:
  for y in nums:
    for z in nums:
      if x + y + z == 2020:
        print(f"Found it! (x,y,z)=({x},{y},{z}). Product: {x*y*z}")

print("All done.")
