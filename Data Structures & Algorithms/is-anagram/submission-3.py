from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = defaultdict(lambda: 0)
        for character in s:
            dict_s[character] += 1

        for element in t:
            if element not in dict_s or dict_s[element] == 0:
                return False
            dict_s[element] -= 1
        
        return True

        