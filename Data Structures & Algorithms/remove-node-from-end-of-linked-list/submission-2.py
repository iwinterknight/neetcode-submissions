# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        i = 0
        while i < n:
            fast = fast.next
            i += 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        if slow != dummy:
            slow.next = slow.next.next
        else:
            head = head.next
        return head
        