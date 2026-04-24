# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum, carry = 0, 0
        p1, p2 = l1, l2
        res = ListNode(0)
        pr = res
        while p1 and p2:
            num1, num2 = p1.val, p2.val
            sum = carry + num1 + num2
            digit = sum % 10
            carry = sum // 10
            pr.next = ListNode(digit)
            pr = pr.next
            p1, p2 = p1.next, p2.next
        while p1:
            sum = carry + p1.val
            digit = sum % 10
            carry = sum // 10
            pr.next = ListNode(digit)
            pr = pr.next
            p1 = p1.next
        while p2:
            sum = carry + p2.val
            digit = sum % 10
            carry = sum // 10
            pr.next = ListNode(digit)
            pr = pr.next
            p2 = p2.next        
        if carry > 0:
            pr.next = ListNode(carry)

        return res.next
