class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumList = []
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            sumList.append(curSum)
        return sumList