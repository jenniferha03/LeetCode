class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2*n)
        val = 0
        for i in range(n): #i = 
            ans[i*2] = nums[i]
            ans[i*2+1] = nums[i+n]
        return ans