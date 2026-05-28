class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Binary Search
        low = 0 # low = 1
        high = len(nums)-1 # high = 1
        if len(nums) == 1:
            return 0
        if nums[low] > nums[low + 1]:
            return low
        if nums[high] > nums[high - 1]:
            return high

        while low <= high: # 0 < 1
            mid = (low + high) // 2 # mid = 0
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] <= nums[mid+1]:
                low = mid + 1
            elif nums[mid] <= nums[mid-1]:
                high = mid - 1
        return -1
    # [3,4,3,2,1]