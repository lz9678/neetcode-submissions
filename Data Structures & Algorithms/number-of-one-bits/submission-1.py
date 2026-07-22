class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # in python, while n is the same as while n!=0
            if n % 2 == 1:
                count += 1
            n //= 2

        return count


        



        