class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        if target > nums[high]:
            return high + 1
        while low < high:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid
            else:
                low = mid + 1
            mid = (low + high) // 2
        return mid