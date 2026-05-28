class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = 0, 0
        nums_hash = {}
        for num in nums:
            if num in nums_hash:
                nums_hash[num] += 1
            else:
                nums_hash[num] = 1
        for i in range(1, len(nums)+1):
            if i in nums_hash:
                if nums_hash[i] == 2:
                    duplicate = i
            else:
                missing = i
        return [duplicate, missing]
        

            