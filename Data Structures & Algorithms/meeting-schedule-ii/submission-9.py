"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        last = []
        last.append(intervals[0].end)
        for i in range(1, len(intervals)):
            cur_start = intervals[i].start
            min_diff = float('inf')
            room = -1
            for j in range(len(last)):
                # find the room whose last meeting ends the late - greedy
                if cur_start >= last[j] and cur_start - last[j] < min_diff:
                    min_diff = cur_start - last[j]
                    room = j
            if room > -1:
                last[room] = intervals[i].end
            else:
                last.append(intervals[i].end)
        return len(last)            





        
        