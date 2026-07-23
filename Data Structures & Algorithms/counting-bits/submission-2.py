class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        
        for i in range(1, n + 1):
            # 先把 i 最右边的一个 1 删除，找到这个较小数字的答案，然后再加上刚刚删除的那个 1。
            dp[i] = dp[i&(i-1)] + 1
        
        return dp
        