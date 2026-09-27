class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)): 
            num_j = target - nums[i]
            
            if num_j in num_dict:
                j = num_dict[num_j]
                return [i, j] if i < j else [j, i]
            num_dict[nums[i]] = i
