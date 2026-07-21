class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 因为题目要返回 所有排列，不是找一个答案，所以本质是：
        # 每一层选一个还没用过的数字，直到 path 长度等于 nums 长度。
        res = []
        cur = []
        n = len(nums)
        used = [False] * n


        def backtrack():
            if len(cur) == n:
                res.append(cur.copy()) # why use .copy() here
                return                

            for i in range(n):
                if used[i]:
                    continue # skip the num which have been used

                # add the new num to the path, and mark it in used[i]
                cur.append(nums[i])
                used[i] = True

                backtrack()

                cur.pop()
                used[i] = False

        backtrack()
        return res
