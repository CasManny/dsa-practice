def minimum_window_substring(s, t):
    need = {}
    for ch in t:
        need[ch] = 1 + need.get(ch, 0)
        
    need_count = len(need)
    window = {}
    left = 0
    have = 0
    res_len, res_l, res_r = float('inf'), 0, 0

    for right, ch in enumerate(s):
        window[ch] = 1 + window.get(ch, 0)
        if ch in need and window[ch] == need[ch]:
            have += 1
        
        while have == need_count:
            if (right - left + 1) < res_len:
                res_len, res_l, res_r = right - left + 1, left, right

            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    return "" if res_len == float("inf") else s[res_l: res_r + 1]

s = "ADOBECODEBANC"
t = "ABC"
print(minimum_window_substring(s, t))
# Output: "BANC