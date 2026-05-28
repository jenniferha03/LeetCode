class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        nums_hash = {}
        for num in nums:
            if num not in nums_hash:
                nums_hash[num] = 1
            else:
                nums_hash[num] += 1
        while k > 0:
            max_val = -1
            max_key = -1001
            for key, value in nums_hash.items():
                if value > max_val:
                    max_val = value
                    max_key = key
            ans.append(max_key)
            nums_hash.pop(max_key)
            k -= 1
        return ans