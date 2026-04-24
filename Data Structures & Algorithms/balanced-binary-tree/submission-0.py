# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def recursive(root):
            if not root:
                return 0

            left = recursive(root.left)
            right = recursive(root.right)

            if abs(left - right) > 1:
                self.balanced = False
            
            return 1 + max(left, right)

        recursive(root)
        return self.balanced