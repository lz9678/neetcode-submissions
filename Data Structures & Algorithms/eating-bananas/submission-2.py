import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_finish(k: int, h: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
                # hours += (pile + k-1)//k

            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2
            if can_finish(mid, h):
                right = mid
            else:
                left = mid + 1

        return left

        

                
                



        