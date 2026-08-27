class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_list = set()
        for num in nums:
            if num in num_list:
                return num
            num_list.add(num)
        