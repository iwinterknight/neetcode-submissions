# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import itertools

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_head = ListNode()
        res_ptr = res_head
        counter = itertools.count()
        ptrs = []
        for i, link_list in enumerate(lists):
            if link_list:
                heapq.heappush(ptrs, (link_list.val, next(counter), link_list))
        while ptrs:
            _, _, min_node = heapq.heappop(ptrs)
            res_ptr.next = min_node
            res_ptr = res_ptr.next
            next_node = min_node.next
            if next_node:
                heapq.heappush(ptrs, (next_node.val, next(counter), next_node))
        
        return res_head.next

        