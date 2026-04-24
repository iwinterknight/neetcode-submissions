# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recursive(root, max_val):
            if not root:
                return 0
            
            good_nodes = 0
            if root.val >= max_val:
                max_val = root.val
                good_nodes += 1

            left = recursive(root.left, max_val)
            right = recursive(root.right, max_val)

            return good_nodes + left + right

        res = recursive(root, root.val)
        return res