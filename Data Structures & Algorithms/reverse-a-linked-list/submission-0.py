# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev, cur, nex = None, head, head.next 
        while nex:
            # save nex.next
            temp = nex.next

            # new direction
            nex.next = cur
            cur.next = prev

            # move to next position
            prev, cur, nex = cur, nex, temp
        return cur

        