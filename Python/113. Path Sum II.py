# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0
    res = []
    path = []
    targetSum = 0

    def dfs(self, node: Optional[TreeNode]) -> None:
        if not node.left and not node.right:
            if self.s + node.val == self.targetSum:
                self.res.append(self.path + [node.val])

            return

        self.path.append(node.val)
        self.s += node.val

        if node.left: self.dfs(node.left)
        if node.right: self.dfs(node.right)

        self.path.pop()
        self.s -= node.val

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []

        self.s = 0
        self.res = []
        self.path = []
        self.targetSum = targetSum
        self.dfs(root)

        return self.res
