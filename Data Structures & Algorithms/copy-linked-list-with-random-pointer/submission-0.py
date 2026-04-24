"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node(0)
        new_ptr = new_head
        ptr = head
        cache = {}
        while ptr:
            new_node = Node(ptr.val)
            cache[ptr] = new_node
            new_ptr.next = new_node
            ptr = ptr.next
            new_ptr = new_ptr.next
        
        ptr, new_ptr = head, new_head.next
        while ptr:
            new_ptr.random = cache.get(ptr.random, None)
            new_ptr = new_ptr.next
            ptr = ptr.next
        
        return new_head.next