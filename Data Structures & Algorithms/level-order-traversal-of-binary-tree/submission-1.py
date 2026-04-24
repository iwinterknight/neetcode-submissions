# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []
            queue = [(root, 1)]
            res = []
            while queue:
                pop, lvl = queue.pop(0)
                if lvl > len(res):
                    res.append([pop.val])
                else:
                    res[-1].append(pop.val)
                    
                if pop.left:
                    queue.append((pop.left, lvl + 1))
                if pop.right:
                    queue.append((pop.right, lvl + 1))
            return res
        
        return bfs(root)