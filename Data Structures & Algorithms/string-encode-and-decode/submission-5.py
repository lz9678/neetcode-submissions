class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): 
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)

            word = ""
            for j in range(i+1, i+1+length):
                word += s[j]
            res.append(word)
            i += length + 1
        return res
        
