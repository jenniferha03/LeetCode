class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums.append(upper + 1)
        output = []
        diff = 0
        for idx in range(len(nums)): #idx = 5
            diff = nums[idx] - lower # diff = 100 - 76 = 24
            if diff > 0:
                output.append([lower, nums[idx]-1])
            lower = nums[idx] + 1
        return output
        