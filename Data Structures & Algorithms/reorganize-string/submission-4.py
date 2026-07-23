from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        # Python 是 Min Heap，所以用负数频率模拟 Max Heap。
        max_heap = [
            (-count, char)
            for char, count in freq.items()
        ]
        heapq.heapify(max_heap)

        result = []

        # 上一轮使用的字符暂时不能再次使用
        prev_count = 0
        prev_char = ""

        # Greedy: 从当前可以使用的字符中，选剩余数量最多的那个。为什么？因为数量最多的字符最难安排。
        while max_heap:
            count, char = heapq.heappop(max_heap)

            # 使用当前剩余次数最多的字符
            result.append(char)

            # count 是负数：
            # -3 + 1 = -2，表示剩余次数从 3 变成 2
            count += 1

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))

            # 当前字符暂时扣住，下一轮不能直接使用
            prev_count = count
            prev_char = char

        # 如果没能使用所有字符，说明不可能完成
        if len(result) != len(s):
            return ""

        return "".join(result)

