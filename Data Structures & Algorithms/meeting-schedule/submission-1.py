"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n <= 1:
            return True

        intervals.sort(key = lambda x:x.start)
        
        last = intervals[0].end
        for i in range(1, n):
            if intervals[i].start < last:
                return False
            last = intervals[i].end

        return True


