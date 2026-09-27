class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        sort_freq = sorted(freq.items(), key = lambda x : x[1], reverse = True)

        res = []
        for key, count in sort_freq:
            if k == 0:
                return res
            res.append(key)
            k -= 1
        
        return res
