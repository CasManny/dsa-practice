def combinationSum(candidates, target):
    result = []

    def backtrack(start, path, total):
        # If the sum matches target, save the path
        if total == target:
            result.append(path[:])
            return
        
        # If sum exceeds target, stop exploring
        if total > target:
            return

        # Explore further candidates
        for i in range(start, len(candidates)):
            # Include candidates[i]
            path.append(candidates[i])
            # Recurse with updated sum, allowing reuse of same element
            backtrack(i, path, total + candidates[i])
            # Backtrack: remove last choice
            path.pop()

    backtrack(0, [], 0)
    return result

print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,2,3,7], 7))
