class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x  
        # x could be 0 sould it is better to start l as 0 not 1
        while l <= r: 
            # 用l<=r而不是l<r
            # 当我们用mid+1和mid-1的时候就要用这个，因为这是最经典的「搜索具体值」模板。
            mid  = l + (r-l)//2  # 这个在C++里更被preferred
            # mid = (l + r) // 2 # 这个也可以
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1 
            else:
                r = mid -1 
            # mid + 1和mid-1并不会跳过答案

        return r # 停在最后一个合法位置。
        # 因为你不是在找“等于”，而是在找 True 和 False 的分界线。
        # 这正是很多二分题最核心的套路。
        
        

        