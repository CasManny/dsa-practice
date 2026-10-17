nums = [1, 1, 1, 2,2,2,2,2,4,5]

def frequentKElement(nums, k):
    count = {}
    
    freqMap = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for number, count in count.items():
        freqMap[count].append(number)

    result = []

    for i in range(len(nums) - 1, -1, -1):
        for number in freqMap[i]:
            result.append(number)
            if len(result) == k:
                return result

print(frequentKElement(nums, 2))

    