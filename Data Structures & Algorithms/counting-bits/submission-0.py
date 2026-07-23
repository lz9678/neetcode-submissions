class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):       
            quotient = num
            count = 0
            while quotient > 0:
                quotient = num // 2
                remainder = num % 2
                if remainder == 1:
                    count += 1
                num = quotient 

            res.append(count)
        return res
        