# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            if not head or not head.next:
                return head
            new_head = reverse(head.next)
            head.next.next = head
            head.next = None
            return new_head


        def reverse_half(head):
            forward_half = head
            fast, slow = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            reverse_half = reverse(slow)
            return forward_half, reverse_half


        forw, revr = reverse_half(head)
        forw_flag = 1
        res = None
        while forw and revr:
            if forw_flag % 2:
                if not res:
                    res = forw
                    ptr = res
                else:
                    ptr.next = forw
                    ptr = ptr.next
                forw = forw.next
            else:
                if not res:
                    res = revr
                    ptr = res
                else:
                    ptr.next = revr
                    ptr = ptr.next
                revr = revr.next
            forw_flag = (forw_flag + 1) % 2
        return res
