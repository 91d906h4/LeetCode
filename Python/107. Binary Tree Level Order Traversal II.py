# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, temp = [], [root]

        while temp:
            l, c = [], []

            for i in temp:
                if i: l.append(i.val); c.append(i.left); c.append(i.right)

            temp = c
            res.append(l)

        return reversed(res[:-1])
