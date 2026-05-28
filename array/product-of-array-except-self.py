class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        zero_count = 0
        period = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                period *= num

        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    ans[i] = period
                else:
                    ans[i] = 0
            elif zero_count > 1:
                ans[i] = 0
            else:
                ans[i] = period // nums[i]
        # print(ans)
        return ans
