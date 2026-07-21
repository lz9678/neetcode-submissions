class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # while 结束时，l 和 r 已经越过了合法 palindrome 的边界
            # 所以真正的 palindrome 是 s[l+1 : r]
            cur = s[l + 1 : r]
            if len(cur) > len(res):
                res = cur

        for i in range(len(s)):
            expand(i, i)       # odd length palindrome
            expand(i, i + 1)   # even length palindrome

        return res
            
        