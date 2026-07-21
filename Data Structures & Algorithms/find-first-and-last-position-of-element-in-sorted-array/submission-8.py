class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # optimal 的做法是做 两次 binary search：
        n = len(nums)
        def find_left():
            left, right = 0, n-1
            res = -1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    res = mid
                    right = mid - 1 # find the leftest
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return res
    
        def find_right():
            left, right = 0, n-1
            res = -1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1 # find the rightest
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return res
      
        return [find_left(), find_right()]

        