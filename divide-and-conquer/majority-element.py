class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = dict()
        for key in nums:
            if key in target:
                target[key] += 1
            else:
                target[key] = 1
        
        for key in target:
            if target[key] > len(nums)//2:
                return key
        