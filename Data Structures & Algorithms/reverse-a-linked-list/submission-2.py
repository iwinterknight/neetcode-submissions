# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(head):
            if not head.next:
                return head
            ptr = recursive(head.next)
            head.next.next = head
            head.next = None
            return ptr
        
        return recursive(head) if head else None