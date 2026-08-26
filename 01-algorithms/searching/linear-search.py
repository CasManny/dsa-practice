def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1
  