class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Because the values are guaranteed to be between 1 and n, 
        # we can treat the array as a Linked List 
        # where the value of a number points to the next index. 
        # A duplicate number means multiple numbers point to the same index, 
        # which creates a cycle

        # 数组的长度是 n + 1，并且数组里面所有的数字都在 [1, n] 的范围内。
        # 数组变成链表
        slow, fast = 0, 0

        # 相遇只是证明了“有环”，但并没有告诉我们“环是从哪里开始的”。
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break 

        # 起点到入口的距离 == 相遇点到入口的距离
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow 

        # 假设起点到入口的距离是 A。
        # 假设入口到相遇点的距离是 B。
        # 假设相遇点继续走完一圈回到入口的距离是 C。
        # 因为快指针的速度是慢指针的两倍（2 * 慢指针路程 = 快指针路程），
        # 2(A + B) = A + B + k (B+C)
        # A + B = kB + kC
        # A = (k-1)B + kC = (k-1)(B+C) + C
        # A = C + (k-1)x环长
        # when k = 1, A = C
        # when k > 2, A = C + 环长
        # 环很小，直路很长，快指针在环里转了好几百圈）
        # slow2 走完距离 A 到达入口时，老 slow 会怎样？
        # 它会先走完距离 C 到达入口，然后在环里空转 n-1 圈，
        # 最后刚好也在同一时刻停在入口处


        
    
        