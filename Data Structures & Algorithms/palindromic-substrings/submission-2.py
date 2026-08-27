class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand(left: int, right: int):
            sub_count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                sub_count += 1
            return sub_count
            
        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i+1)
        
        return count
