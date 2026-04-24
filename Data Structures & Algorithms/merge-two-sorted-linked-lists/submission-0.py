# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        res, ptr = None, None
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                if not res:
                    res = ptr1
                    ptr = res
                else:
                    ptr.next = ptr1
                    ptr = ptr.next
                ptr1 = ptr1.next
            else:
                if not res:
                    res = ptr2
                    ptr = res
                else:
                    ptr.next = ptr2
                    ptr = ptr.next
                ptr2 = ptr2.next
        while ptr1:
            if not res:
                res = ptr1
                ptr = res
            else:
                ptr.next = ptr1
                ptr = ptr.next
            ptr1 = ptr1.next
        while ptr2:
            if not res:
                res = ptr2
                ptr = res
            else:
                ptr.next = ptr2
                ptr = ptr.next
            ptr2 = ptr2.next
        return res
