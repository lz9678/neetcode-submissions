class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            bit = n%2
            res = res * 2 + bit
            n //= 2

        return res

        
