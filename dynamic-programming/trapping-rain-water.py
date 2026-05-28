class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right, total = 0, 0, 0
        max_rights = [0] * len(height)
        for idx in range(len(height)-1, 0, -1):
            max_rights[idx] = max_right
            max_right = max(height[idx], max_right)
        for idx, val in enumerate(height):
            max_right = max_rights[idx]
            water = min(max_left, max_right) - val
            max_left = max(val, max_left)
            total += max(water, 0) 
        return total