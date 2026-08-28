class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        num = n // 3
        remain = n % 3
        if remain == 0:
            return 3**num
        
        if remain == 1:
            return 3**(num-1) * 4

        return 3**num * 2
