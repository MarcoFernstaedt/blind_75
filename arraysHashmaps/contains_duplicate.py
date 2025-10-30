def has_duplicate(nums):
    uniqueNums = set()
    for num in nums:
        if num in uniqueNums:
            return True
        uniqueNums.add(num)
    return False


for arr in [[1, 2, 3, 4], [1, 2, 3, 1], [10, 5, 2, 10, 8, 5], [7]]:
    print(arr, "->", has_duplicate(arr))
