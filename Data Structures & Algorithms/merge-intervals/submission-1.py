class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return [[intervals[0][0],intervals[0][1]]]
        
        intervals.sort(key = lambda x: x[0])
        res = []
        left, right = intervals[0][0],intervals[0][1]
        res.append([left, right])
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start > right: # no overlap
                # adding the interval to res
                res.append([start, end])
                # update pointers
                left, right = start, end
            else: # has overlap (current interval with the last interval)
                # get the largest end point
                right = max(end, right)
                # update the end of the last interval
                res[-1][-1] = right
        
        return res
