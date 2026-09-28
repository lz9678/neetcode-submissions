class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
            
        nums_s = sorted(nums)
        long = 1
        cur = 1
        for i in range(1, len(nums_s)):
            if nums_s[i] - nums_s[i-1] == 1:
                cur += 1
            if nums_s[i] - nums_s[i-1] > 1:
                cur = 1
            long = max(long, cur)

        return long
   

