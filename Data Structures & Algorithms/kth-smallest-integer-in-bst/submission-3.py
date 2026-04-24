# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, k):
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if k == 1:
                    return root.val
                k -= 1
                root = root.right

        return inorder(root, k)
                
