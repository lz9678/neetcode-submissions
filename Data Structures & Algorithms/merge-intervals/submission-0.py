class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        # all intervals: min of start point, max of end point
        # non-overlapping
        result = []

        # 按照区间的 start (即 x[0]) 进行升序排序 需要这一步吗？
        intervals.sort(key=lambda x:x[0])
        
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            # 如果 result 为空，或者当前区间的起点 > result里最后一个区间的终点
            # 说明没有重叠，直接放入 result
            if not result or start > result[-1][1]:
                result.append(interval)
            else:
                # 否则说明有重叠，需要合并！
                # 更新 result 里最后一个区间的终点，取两者终点的最大值
                result[-1][1] = max(end, result[-1][1])


        return result