# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r = []
        q = [root]

        if not root: return []

        while q:
            t, n = [], []

            while q:
                x = q.pop(0)

                if x:
                    t.append(x.val)
                    if x.left: n.append(x.left)
                    if x.right: n.append(x.right)

            r.append(t)
            q = n

        return r
