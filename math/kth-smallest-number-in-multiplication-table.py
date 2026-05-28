class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            count = 0
            for i in range(1, m+1):
                count += min(n, x // i)
            return count

        ans = 0
        l, r = 1, m*n
        while l <= r:
            mid = (l + r) // 2
            if count(mid) >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans