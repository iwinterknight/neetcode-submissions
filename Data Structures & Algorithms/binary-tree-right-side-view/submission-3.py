# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs_1(root):
            res = []
            q = [root]
            while q:
                rightSide = None
                qLen = len(q)
                for i in range(qLen):
                    node = q.pop(0)
                    if node:
                        rightSide = node
                        q.append(node.left)
                        q.append(node.right)
                if rightSide:
                    res.append(rightSide.val)
            return res


        def bfs_2(root):
            if not root:
                return []
            queue = [(root, 1)]
            res = []
            while queue:
                pop, lvl = queue.pop(0)
                if lvl > len(res):
                    res.append([pop.val])
                else:
                    res[-1].append(pop.val)
                    
                if pop.left:
                    queue.append((pop.left, lvl + 1))
                if pop.right:
                    queue.append((pop.right, lvl + 1))
            return res
        

        return bfs_1(root)

        # res = []
        # bfs_res = bfs_1(root)
        # for item in bfs_res:
        #     res.append(item[-1])
        # return res
