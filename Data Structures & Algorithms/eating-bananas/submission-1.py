import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The minimum possible speed is 1
        # The maximum useful speed is the size of the largest pile
        left, right = 1, max(piles)  # speed
        result = 0

        while left <= right:
            mid = left + (right-left)//2
            # time for a single pile
            total_hr = 0
            for pile in piles:
                total_hr += math.ceil(pile/mid)
            
            if total_hr <= h:
                result = mid
                right = mid-1
            else:
                left = mid+1

        return min(result, left)









