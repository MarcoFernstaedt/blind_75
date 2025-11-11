def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


tests = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),  # target present (middle-right)
    ([-1, 0, 3, 5, 9, 12], 2, -1),  # target missing
    ([1], 1, 0),  # single element found
    ([1], 0, -1),  # single element not found
    ([2, 5], 2, 0),  # small array, first element
    ([2, 5], 5, 1),  # small array, second element
    ([2, 5], 3, -1),  # small array, missing
]

for nums, target, expected in tests:
    result = search(nums, target)
    print(
        f"{nums}, target={target} -> {result}  ({'OK' if result == expected else 'FAIL, expected ' + str(expected)})"
    )
