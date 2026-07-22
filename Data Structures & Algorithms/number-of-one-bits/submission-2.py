class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1

        return count

# 判断一个数是奇数还是偶数，其实就是看二进制最后一位：偶数最后一位都是0，奇数最后一位都是1
# Bitwise AND: 把两个数都写成二进制，然后一位一位比较(只有两个都是1，结果才是1)
# 1的二进制是0001
# 如果这个数是奇数，和1的Bitwise AND的最后一位就是1
# 如果这个数是偶数，和1的Bitwise AND的最后一位就是0
# 而且因为1的二进制除了最后一位全是0，所以任何和他Bitwise AND的结果除了最后一位也肯定都是0





        