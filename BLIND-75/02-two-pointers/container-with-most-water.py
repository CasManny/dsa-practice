def container_with_most_water(heights):
    max_area = 0
    left, right = 0, len(heights) - 1
    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        max_area = max(area, max_area)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(container_with_most_water(heights))



   