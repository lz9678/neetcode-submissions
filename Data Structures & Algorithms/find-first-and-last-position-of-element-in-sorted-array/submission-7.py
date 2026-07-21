class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0,0] if nums[0] == target else [-1,-1]

        left, right = 0, n-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                cur = mid
                while cur >=1 and nums[cur] == nums[cur-1]:
                    cur -= 1
                res_l = cur
                cur = mid
                while cur <= n-2 and nums[cur] == nums[cur+1]:
                    cur += 1
                res_r = cur
                return [res_l, res_r]
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return [-1, -1]





        