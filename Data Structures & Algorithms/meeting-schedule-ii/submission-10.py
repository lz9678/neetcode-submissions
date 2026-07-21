"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        # 开始时间相当于“需要一个房间” (+1)
        # 结束时间相当于“释放一个房间” (-1)
        for i in intervals:
            events.append((i.start, 1))
            events.append((i.end, -1))
        
        # 按照时间顺序排序；如果时间相同，先下车(-1)再上车(+1)，避免多算房间
        events.sort(key = lambda x: (x[0], x[1]))

        rooms = 0
        max_rooms = 0
        for time, action in events:
            rooms += action
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms




        
        