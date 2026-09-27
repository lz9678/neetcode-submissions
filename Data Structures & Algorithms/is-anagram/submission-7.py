from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sort_s = sorted(s)
        sort_t = sorted(t)
        for s_char, t_char in zip(sort_s, sort_t):
            if s_char != t_char:
                return False

        return True


        