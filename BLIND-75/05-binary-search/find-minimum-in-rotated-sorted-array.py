def find_minimum_in_rotated_sorted_arr(nums):
    res = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break
         
        m = left + (right - left) // 2
        res = min(res, nums[m])

        if nums[m] >= nums[left]:
            left = m + 1
        else:
            right = m - 1
    return res

print(find_minimum_in_rotated_sorted_arr([6, 8, 9, 2, 3, 5]))