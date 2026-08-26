def search_in_rotated_sort_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
            return mid
        
        # left portion
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

print(search_in_rotated_sort_array([5, 6, 8, 0, 2, 3], 2))
        
