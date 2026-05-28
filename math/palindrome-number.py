class Solution:
    def isPalindrome(self, x: int) -> bool:
        khue = 0
        phat = x
        while x > 0:
            n = x % 10
            khue = khue * 10 + n
            x = x //10
        return phat == khue
