class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = nums.sort()
         #Time: O(nlogn)
        if len(nums) <= 1:
            return len(nums)
        curr_sequence = 1
        longest_sequence = 1
        nums.sort()
        for idx in range(1, len(nums)): #curr = 4, longest = 5
            if nums[idx] == nums[idx-1]:
                continue
            if nums[idx] == nums[idx-1] + 1:
                curr_sequence += 1
            else:
                curr_sequence = 1
            if curr_sequence > longest_sequence:
                longest_sequence = curr_sequence
        return longest_sequence