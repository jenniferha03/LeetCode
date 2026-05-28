class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        nums_hash = {}
        sorted_nums = sorted(nums) #sort() time complexity O(nlogn)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in nums_hash:
                nums_hash[sorted_nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in nums_hash:
                ans[i] = nums_hash[nums[i]]
        return ans