class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序来方便之后的去重
        nums.sort()
        res = []
        n = len(nums)

        # 遍历nums寻找第一个数
        for i in range(n):
            # 如果出现重复的数，直接跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 因为数字已经被排序，如果出现正数，后面的数只会更大，不可能加为0，所以跳过
            if nums[i] > 0:
                break 

            # 把triplet的后面两个数作为指针
            left, right = i + 1, n - 1
            while left < right: # 两个数不能重合，所以条件是left < right
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]: #跳过重复的left指针
                        left += 1
                    while left < right and nums[right] == nums[right-1]: #跳过重复的right指针
                        right -= 1
                    left += 1
                    right -= 1
                    #  break 一个i可能会有多个triplet不能用break
                elif total > 0:
                    right -= 1
                else: # total < 0
                    left += 1

        return res