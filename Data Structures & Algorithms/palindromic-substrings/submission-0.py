class Solution:
    def countSubstrings(self, s: str) -> int:

        def is_palin (s: str) -> bool:
            # list_s = list(s)   # str不需要list也可以直接indexing
            l, r = 0, len(s)-1
            while l <= r:
                # if list_s[l] != list_s[r]:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        num_subs = 0
        # start point
        for i in range(len(s)):
            # end point
            for j in range(i, len(s)):
                if is_palin(s[i:j+1]):
                    num_subs +=1
        
        return num_subs





