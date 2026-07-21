class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # each element: length of the subsequence which ends with this num
        # nums = [9,1,4,2,3,3,7]
        # dp[0]: length of the subsequence ends with 9
        # n states 
        # each state just means the state when the subsequence ends with this number
        dp = [1] * len(nums)

        # 确定当前要计算的数 nums[i]
        for i in range(n):
            # 回头看 i 之前的所有数
            for j in range(i):
                # 只有当后面的数大于前面的数，满足严格递增时，才能拼接
                if nums[i] > nums[j]:
                    # 看看是保持目前的 dp[i] 大，还是把 nums[i] 接在 nums[j] 后面大
                    dp[i] = max(dp[i], dp[j]+1) 
                
        # 最长递增子序列可能以任何一个元素结尾，所以在 dp 数组里找最大值
        return max(dp)


        

