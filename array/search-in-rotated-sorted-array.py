class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1	  
            else:
                r = mid


        def binarySearch(left, right):	
            while left <= right:		
                middle = (left + right) // 2
                if nums[middle] == target: 
                    return middle
                elif nums[middle] < target: 
                    left = middle + 1
                else:					
                    right = middle - 1
            return -1

        ans1 = binarySearch(0, l-1)
        ans2 = binarySearch(l, len(nums)-1)
        
        if ans1 != -1 and ans2 == -1:
            return ans1
        elif ans1 == -1 and ans2 != -1:
            return ans2
        else:
            return -1
