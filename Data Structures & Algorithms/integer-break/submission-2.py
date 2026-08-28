class Solution:
    def integerBreak(self, n: int) -> int:
        # 把整数 i 拆成至少两个正整数后，能得到的最大乘积。 
        dp = [0] * (n+1)

        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])

        return dp[n]

        