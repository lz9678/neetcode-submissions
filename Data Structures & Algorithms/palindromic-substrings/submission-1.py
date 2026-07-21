class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand_around_center (l: int, r: int) -> int:
            count = 0
            # 当左右指针没有越界，并且两边字符相等时，继续扩展
            while l >= 0 and r <=  len(s)-1 and s[l] == s[r]:
                count += 1
                l -= 1   # 左指针左移
                r += 1   # 右指针右移
            return count

        num_subs = 0
        for i in range(len(s)):
            num_subs += expand_around_center(i,i)
            num_subs += expand_around_center(i,i+1)
        
        return num_subs





