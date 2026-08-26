def two_sum(arr, target):
    seen = {}
    
    for index, value in enumerate(arr):
        complement = target - value
        
        if complement in seen:
            return [seen[complement], index]

        seen[value] = index

arr = [1, 19, 18, 20]
print(two_sum(arr, 21))






