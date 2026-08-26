def longestSubstringWithoutRepeatingchar(s):
    longest = 0
    seen = set()
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        longest = max(longest, right - left + 1)
    print(seen)
    return longest

print(longestSubstringWithoutRepeatingchar("abcbbcbcde"))


        
