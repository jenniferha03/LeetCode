class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for num in nums1:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for num in nums2:
            if num in d and d[num] > 0:
                d[num] -= 1
                res.append(num)
            else:
                continue
        return res
            
