def topKFrequentElement(nums, k):
    count = {}
    freq_map = [[] for _ in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    for value, c in count.items():
        freq_map[c].append(value)

    
    res = []
    
    for i in range(len(freq_map) - 1, 0, -1):
        for ch in freq_map[i]:
            res.append(ch)
            if len(res) == k:
                return res
            
    return []

nums = [1, 1, 1, 2, 2, 3, 4]
print(topKFrequentElement(nums, 2))
            
            
