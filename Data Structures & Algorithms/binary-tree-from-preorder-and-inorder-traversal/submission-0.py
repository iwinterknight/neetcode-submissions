# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder):
            if not inorder or not preorder:
                return None

            root_val = preorder[0]
            root_idx = inorder.index(root_val)
            left_subtree = build(preorder[1:root_idx+1], inorder[:root_idx])
            right_subtree = build(preorder[root_idx+1:], inorder[root_idx+1:])
            return TreeNode(root_val, left_subtree, right_subtree)

        return build(preorder, inorder)