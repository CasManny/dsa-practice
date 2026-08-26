def longestRepeatingChaReplacement(s, k):
    max_freq = 0
    count = {}
    left = 0
    max_length = 0

    for right, ch  in enumerate(s):
        count[ch] = 1 + count.get(ch, 0)
        max_freq = max(max_freq, count[ch])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
    return max_length
s = "AABABBA"
k = 1


print(longestRepeatingChaReplacement(s,k))

