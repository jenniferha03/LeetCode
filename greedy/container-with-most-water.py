class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, curr_water, most_water = 0, 0, 0
        end = len(height)-1
        while start < end:
            curr_water = min(height[start], height[end]) * (end-start)
            if curr_water > most_water:
                most_water = curr_water
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return most_water