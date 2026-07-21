class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])

        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]

            inter_start = max(start1, start2)
            inter_end = min(end1, end2)

            if inter_end - inter_start >= duration:
                return [inter_start, inter_start + duration]
            
            if end1 <  end2:
                i += 1
            else:
                j += 1

        return []




        