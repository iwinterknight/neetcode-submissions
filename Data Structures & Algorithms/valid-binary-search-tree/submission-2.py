# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursive(root, min_val=float('-inf'), max_val=float('inf')) -> bool:
            if not root:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            left = recursive(root.left, min_val, root.val)
            right = recursive(root.right, root.val, max_val)

            if left and right:
                return True
            return False

        return recursive(root)