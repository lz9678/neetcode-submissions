class Solution:
    def reverseBits(self, n: int) -> int:
        n_string = bin(n)[2:].zfill(32)
        res = 0
        for i in range(0, len(n_string)):
            res += int(n_string[i]) * (2**i)
        return res 