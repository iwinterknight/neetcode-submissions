# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def range_based_recursion(root, minVal=float('-inf'), maxVal=float('inf')):
            if not root:
                return True

            if root.val <= minVal or root.val >= maxVal:
                return False

            return range_based_recursion(root.left, minVal, root.val) and range_based_recursion(root.right, root.val, maxVal)


        return range_based_recursion(root)