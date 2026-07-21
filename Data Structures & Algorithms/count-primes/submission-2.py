class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0  # 严格小于2的没有质数

        # 初始化一个长度为 n 的布尔数组，全部设为 True
        is_prime = [True] * n
        # 0 和 1 不是质数
        is_prime[0] = False
        is_prime[1] = False 

        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                # 如果 i 是质数，把 i 的倍数（从 i*i 开始）全标记为 False
                for j in range(i*i, n, i):
                    is_prime[j] = False

        # 假设我们现在遍历到了质数 i = 5。我们要把 5 的倍数都标记为 False（非质数）。
        # 5 的倍数依次是：2*5, 3*5, 4*5, 5*5, 6*5...
        # 如果你从 2 * 5 开始标记，会发生什么？ 你会把 10 标记为 False
        # 对于 k * 5，只要系数 k < 5（也就是 k 为 2, 3, 4）这个乘积必定包含一个比 5小的质因数。
        # 而我们是从小到大遍历质数的，所以这些数早就被前面那些小质数给“清理”掉了。

        # 统计依然为 True 的个数，即为质数个数
        return sum(is_prime)

                    
        