def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i


nums = [1, 2, 15, 33]
target = 16
print(two_sum(nums, target))
