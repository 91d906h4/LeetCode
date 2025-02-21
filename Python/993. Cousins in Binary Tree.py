# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        p = []

        while q:
            temp = {}

            for t in q:
                if t.left:
                    temp[t.left.val] = t.val
                    p.append(t.left)

                if t.right:
                    temp[t.right.val] = t.val
                    p.append(t.right)

            if x in temp and y in temp:
                if temp[x] == temp[y]:
                    return False

                return True

            q = p
            p = []

        return False
