# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def recursive(root, max_sum):
            if not root:
                return 0

            left_sum = max(recursive(root.left, max_sum), 0)
            right_sum = max(recursive(root.right, max_sum), 0)
            max_sum[0] = max(max_sum[0], left_sum + right_sum + root.val)
            return root.val + max(left_sum, right_sum)


        max_sum = [root.val]
        recursive(root, max_sum)
        return max_sum[0]

            