# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        cur1 = list1
        cur2 = list2

        if cur1.val <= cur2.val: 
            new_head = cur1
            cur = cur1 
            cur1 = cur1.next
        else:
            new_head = cur2
            cur = cur2
            cur2 = cur2.next

        while cur1 or cur2:
            if cur1 and not cur2: 
                cur.next = cur1 
                cur1 = cur1.next
            elif cur2 and not cur1:
                cur.next = cur2
                cur2 = cur2.next
            elif cur1.val <= cur2.val:
                cur.next = cur1 
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
            
        return new_head