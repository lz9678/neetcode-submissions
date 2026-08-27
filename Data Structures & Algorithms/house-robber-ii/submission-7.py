class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]


        def rob_line(s: List[int]):
            n = len(s)
            if n == 1:
                return s[0]

            prev2, prev1 = s[0], max(s[0], s[1])
            for i in range(2, n):
                cur = max(prev1, prev2 + s[i])
                # prev2 = prev1
                # prev1 = cur
                prev2, prev1 = prev1, cur
            
            return prev1

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))