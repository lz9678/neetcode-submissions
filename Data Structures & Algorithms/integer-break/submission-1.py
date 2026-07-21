class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] will store the max product for integer i
        dp = [0] * (n + 1)
        
        # Base case
        dp[1] = 1
        
        # Fill the dp array from 2 up to n
        for i in range(2, n + 1):
            # We only need to check up to i // 2 because after that, 
            # combinations just reverse (e.g., 1+3 is the same as 3+1)
            for j in range(1, (i // 2) + 1):
                
                # We compare:
                # 1. The current best max product (dp[i])
                # 2. Breaking into two numbers only: j * (i - j)
                # 3. Breaking j, but breaking down (i-j) further: j * dp[i - j]
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
                
        return dp[n]