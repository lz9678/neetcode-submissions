class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in nums:
            if num not in nums_set:
                return num
            else :
                nums_set.remove(num)
