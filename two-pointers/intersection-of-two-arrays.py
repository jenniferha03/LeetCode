class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        s = set()
        for i in nums1:
            if i not in s:
                s.add(i)
            else:
                continue
        for i in nums2:
            if i in s and i not in res:
                res.append(i)
            else:
                continue
        return res
