class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:].zfill(32)

        return sum (
            int(bit) * (2**i)
            for i, bit in enumerate(bits)
        )