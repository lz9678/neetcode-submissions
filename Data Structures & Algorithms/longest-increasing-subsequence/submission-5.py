class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] => 以 nums[i] 结尾的最长 increasing subsequence 的长度。
        # dp = [[0] * len(nums) for _ in len(nums)]
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    dp[i] = max(dp[i], dp[prev]+1)
        return max(dp)