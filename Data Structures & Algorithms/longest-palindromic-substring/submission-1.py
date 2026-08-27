class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩展”是：把每一个位置都当成可能的中心试一遍。
        res = ''

        def expand(left: int, right: int) -> str:
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # while 停下来时，left 和 right 已经多走了一步
            return s[left + 1 : right]

        for i in range(len(s)):
            p1 = expand(i, i)
            p2 = expand(i, i+1)

            if len(p1) > len(res):
                res = p1
                
            if len(p2) > len(res):
                res = p2
    
        return res


        