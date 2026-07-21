class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 每一层选一个还没用过的数字，直到 path 长度等于 nums 长度。
        res = []
        path = []
        n = len(nums)
        used = [False] * n


        def backtrack():
            if len(path) == n:
                # 把当前 path 的内容复制一份，作为独立答案保存下来。
                # 这样后面 path.pop()、path.append() 再怎么改，都不会影响已经存进 res 的答案。
                res.append(path.copy()) 
                return                

            for i in range(n):
                if used[i]:
                    continue # skip the num which have been used

                # 选择
                path.append(nums[i])
                used[i] = True

                # 递归
                backtrack()

                # 撤销选择
                path.pop()
                used[i] = False

        backtrack()
        return res
