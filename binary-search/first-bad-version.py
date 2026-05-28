# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # [1,2,3,....,n]
        left = 1
        right = n

        while left < right:
          mid = (left + right) // 2

          if isBadVersion(mid) == True:
            right = mid
          else:
            left = mid + 1
        return right