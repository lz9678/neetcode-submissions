class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r: # why <= not <
            mid  = l + (r-l)//2 
            # mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1 # won't this skip the nearest?
            else:
                r = mid -1  # won't this skip the nearest?

        return r # why r?
        
        

        