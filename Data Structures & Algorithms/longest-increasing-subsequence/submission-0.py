class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 如果我要进行下一步，我到底需要知道过去发生的哪些事情？
        # 如果是最长递增子序列：我需要知道“上一个放进序列的数字到底是多少”。
        # dp[i][last_index] 表示最长子序列长度，而last_index直接表示子序列最后一个数字在nums中的index
        # 也可以直接写成dp[last_index]
        n = len(nums)
        # nums有多少个数字，就有多少个状态 => 每个状态表示 最长子序列是以这个数字结
        # 用来存已经计算过的状态，避免重复计算
        memo = [[-1]*(n+1) for _ in range(n)]

        # 决定当前的nums[i]是否要选入子序列，last_index是目前最后一个被选入的数字的index
        def dfs(i, last_index):
            if i == n:
                return 0

            if memo[i][last_index+1]!= -1:
                return memo[i][last_index+1]

            # 不选 nums[i]，那么 last_index 保持不变，去处理下一个
            not_take = dfs(i+1, last_index)

            # 选nums[i]，但前提是合法（要么还没选过数字，要么当前数字大于上一个选的数字
            take = 0
            if last_index == -1 or nums[i] > nums[last_index]:
                # 如果选了，长度 + 1，同时 last_index 变成了当前的 i ！
                take = 1 + dfs(i+1, i)

            # 比较选和不选两种情况
            memo[i][last_index + 1] = max(not_take, take)
            return memo[i][last_index+1]

        # 从 index 0 开始，此时什么都没选（上一个 index 是 -1
        return dfs(0, -1)








        