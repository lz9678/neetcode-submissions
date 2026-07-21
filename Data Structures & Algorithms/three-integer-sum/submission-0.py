class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        for i in range(len(nums)):
            for j in range(len(nums)):
                if  i != j:
                    num1, num2 = nums[i], nums[j]
                    diff = - (num1+num2)
                    if diff in nums_dict:
                        k = nums_dict[diff]
                        if k != j and k != i:                                   
                            cur = tuple(sorted([diff, num1, num2]))
                            if cur not in res:
                                res.add(cur)
                                
        return [list(t) for t in res]

        