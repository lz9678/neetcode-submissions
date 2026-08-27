class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]


        def rob_line(s: List[int]):
            n = len(s)
            if n == 1:
                return s[0]
            dp = [0] * n
            dp[0] = s[0]
            dp[1] = max(s[0], s[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + s[i])
            return dp[n-1]

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))