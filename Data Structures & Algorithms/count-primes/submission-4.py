class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False   # 0
        is_prime[1] = False   # 1

        for i in range(2, int(n**0.5)+1): # starts at 2
            if is_prime[i]:
                for j in range(i*i, n, i):
                    # 2: 2x2, 2x3, 2x4, .... n
                    is_prime[j] = False

        return sum(is_prime)
            



        

        