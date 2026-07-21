class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x:x[0])
        slots2.sort(key = lambda x:x[0])
        i, j = 0, 0

        res = []
        
        while  i < len(slots1) and j < len(slots2):
            left1, right1 = slots1[i][0], slots1[i][1]
            left2, right2 = slots2[j][0], slots2[j][1]

            if right1 < left2: # no overlap
                # move the slot 1 but keep the slot 2
                i+= 1
            elif right2 < left1:  # no overlap
                # move the slot2 but keep the slot 1
                j+= 1
            else: # has overlap
                start = max(left1, left2)
                end = min(right1, right2)
                if start + duration <= end:
                    return [start, start + duration]

                if right1 < right2:
                    i += 1
                elif right1 > right2:
                    j += 1
                else:
                    i += 1
                    j += 1
        return []




            
                

            
            
