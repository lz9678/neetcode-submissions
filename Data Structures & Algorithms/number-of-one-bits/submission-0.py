from collections import deque

class Solution:
    def hammingWeight(self, n: int) -> int:
        num = n
        bits = deque()
        count = 0
        while num > 0:
            quotient = num//2
            bits.appendleft(num%2)
            num = quotient
        for bit in bits:
            if bit == 1:
                count += 1

        return count


        



        