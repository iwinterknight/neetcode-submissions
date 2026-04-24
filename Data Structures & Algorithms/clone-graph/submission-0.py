"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        hash_map = {}
        def recursive(node):
            if not node:
                return None
            new_node = Node(node.val)
            hash_map[node] = new_node
            for neighbor in node.neighbors:
                if neighbor in hash_map:
                    cloned_graph_neighbor = hash_map[neighbor]
                else:
                    cloned_graph_neighbor = recursive(neighbor)
                new_node.neighbors.append(cloned_graph_neighbor)
            return new_node
                
        return recursive(node)