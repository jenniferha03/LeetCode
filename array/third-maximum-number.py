class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        i = 0
        largest_max, second_max, third_max = nums[i], float('-inf'), float('-inf')
        
        while i < len(nums): 
            if nums[i] > largest_max: 
                third_max, second_max, largest_max = second_max, largest_max, nums[i] 
            elif nums[i] < largest_max and nums[i] > second_max: 
                third_max, second_max = second_max, nums[i]
            elif nums[i] < second_max and nums[i] > third_max:
                third_max = nums[i]
            i += 1
    
        if third_max == float('-inf'):
            return largest_max
        else:
            return third_max
