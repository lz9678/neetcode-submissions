class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        #4: 2+2
        #5: 2+3
        #6: 3+3
        #7: 3+2+2
        #11: 3+3+3+2

        quotient = n//3
        remainder = n%3

        if remainder == 0:
            return 3**quotient
        elif remainder == 1:
            # combine 3 with 1 to get 4 and then break down into 2 and 2
            return 3**(quotient-1) * 4
        else:
            return 3**quotient * 2

