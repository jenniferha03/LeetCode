class Solution:
    def climbStairs(self, n: int) -> int:
        # 0 1 2 3 ... (k-3) (k-2) (k-1) k
        # f(0) f(1) f(2) f(3) ... f(k-3) f(k-2) ... f(i)
        # dp[i]: number of ways to get to step i
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
