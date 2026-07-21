class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 在 DP 中，我们是“全局统筹”。但在贪心算法里，我们只讲究一个道理：“结尾的数字越小，后面能接上新数字的概率就越大。”
        # 比如同样是长度为 3 的子序列。序列 A 是 [10, 20, 100] 序列 B 是 [1, 2, 3]
        # 贪心算法认为：我根本不需要记住序列 A！既然它们长度都是 3，序列 B 结尾是 3，比 100 小多了，后面随便来个 4、5 都能接上。所以在同等长度下，我永远只保留那个结尾最小的组合。
        
        # tails[i]: 所有长度为 i+1 的递增子序列中，结尾最小的那个数字。
        tails = [] 

        # 确定当前要计算的数 nums[i]
        for num in nums:
            # 使用二分查找，在 tails 中寻找第一个 >= num 的位置
            left, right = 0, len(tails)-1

            while left <= right:
                mid = (left + right)//2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            # 情况 1：如果 left 等于 tails 的长度，说明 num 比里面所有数字都大
            if left == len(tails):
                tails.append(num)
            # 情况 2：替换掉那个比 num 大的数字，让那个位置的“门槛”变低
            else:
                tails[left] = num

        # tails 的长度就是牌堆的数量，也就是最长递增子序列的长度
        return len(tails)

        

