# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive(root):
            if not root:
                return None
            
            node = TreeNode(root.val)
            if root.left:
                node.right = recursive(root.left)
            if root.right:
                node.left = recursive(root.right)
            return node

        return recursive(root)

