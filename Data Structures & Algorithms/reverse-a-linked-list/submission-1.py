# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev, cur = None, head 
        while cur:
            # save nex.next
            temp = cur.next

            # new direction
            cur.next = prev

            # move to next position
            prev, cur = cur, temp
        return prev

        