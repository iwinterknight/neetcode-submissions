# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(preorder, inorder):
            if not preorder or not inorder:
                return None
            item = preorder[0]
            idx = inorder.index(item)
            left_subtree = construct(preorder[1:idx+1], inorder[:idx])
            right_subtree = construct(preorder[idx+1:], inorder[idx+1:])
            return TreeNode(item, left_subtree, right_subtree)


        return construct(preorder, inorder)