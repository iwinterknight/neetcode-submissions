# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left_subtree = self.invertTree(root.right)
        right_subtree = self.invertTree(root.left)

        root.left = left_subtree
        root.right = right_subtree

        return root