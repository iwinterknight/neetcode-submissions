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
            ptr = reverse(head.next)
            head.next.next = head
            head.next = None
            return ptr

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = reverse(slow)

        while left and right:
            nxt_left = left.next
            nxt_right = right.next
            left.next = right
            right.next = nxt_left
            left = nxt_left
            right = nxt_right
            if nxt_right == slow:
                break

