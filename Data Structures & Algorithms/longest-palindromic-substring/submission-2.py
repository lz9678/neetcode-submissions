class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩展”是：把每一个位置都当成可能的中心试一遍。
        start, max_len = 0, 1

        def expand(left: int, right: int) -> str:
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # while 停下来时，left 和 right 已经多走了一步
            return left + 1, right-1 # O(1) space complexity optimize

        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i+1)

            if r1-l1 + 1 > max_len:
                start, max_len = l1, r1-l1+1
                
            if r2-l2 + 1 > max_len:
                start, max_len = l2, r2-l2+1
    
        return s[start:start+max_len]


        