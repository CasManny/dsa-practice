from typing import List

nums_1 = [2, 6, 9, 0, 0, 0]
nums_2 = [-1,3,10]


def merge_two_sorted_array(nums1: List[int], n: int, nums2: List[int], m: int) -> None:
    i, j, k = n - 1, m - 1, m + n - 1
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

merge_two_sorted_array(nums_1, 3, nums_2, 3)
print(nums_1)
    

