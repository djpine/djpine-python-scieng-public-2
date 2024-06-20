import random
# Make a list of k integers randomly chosen from range
nums = random.choices(range(-1000, 1000), k=10)
print(nums)

max = nums[0]
for n in nums:
    if n > max:
        max = n
print("The maximum value is", max)
