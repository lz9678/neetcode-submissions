class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 不是所有“找重复数字”都能用 Floyd cycle detection
        # 这题能用，是因为Each integer in nums is in the range [1, n] inclusive.
        # 所以nums[i] 可以天然当作“下一个节点的 index”。
        slow, fast = 0, 0
        # fast 进入环之后会一直绕圈，slow 也会进入环，只是走得更慢。
        # 因为 fast 每轮比 slow 多走一步，所以它最终一定会“追上” slow。
        # 但追上的位置可能是环里的任何一个点，不一定刚好是入口。
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow







        
