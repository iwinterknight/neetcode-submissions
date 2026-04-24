# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def fetch_min_node(ptrs):
            min_node = None
            min_val, min_idx = float('inf'), None
            for i, ptr in enumerate(lists):
                if ptr:
                    if ptr.val < min_val:
                        min_val = ptr.val
                        min_idx = i
                        min_node = ptr
            ptrs[min_idx] = ptrs[min_idx].next
            return min_node

        res = None
        n = len(lists)
        while lists != [None] * n:
            if not res:
                res = fetch_min_node(lists)
                ptr = res
            else:
                ptr.next = fetch_min_node(lists)
                ptr = ptr.next
        return res
        


        
        
        