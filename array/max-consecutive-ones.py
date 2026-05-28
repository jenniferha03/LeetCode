class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, max_ones = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                if curr > max_ones:
                    max_ones = curr
                curr = 0
        if curr > max_ones:
            max_ones = curr
        return max_ones            