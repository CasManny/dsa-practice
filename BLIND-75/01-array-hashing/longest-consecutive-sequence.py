def longest_consecutive_sequence(nums):
    max_longest = 0
    num_set = set(nums)

    for num in nums: 
        if num - 1 not in num_set:
            length = 0
            while num + length in num_set:
                length += 1
            max_longest = max(max_longest, length)

    return max_longest

print(longest_consecutive_sequence([1, 2, 3, 4, 5, 9, 10, 12, 11])) 