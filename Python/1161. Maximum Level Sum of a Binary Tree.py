# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.values = {}

    def dfs(self, root: Optional[TreeNode], level: int) -> None:
        if root:
            if level not in self.values: self.values[level] = root.val
            else: self.values[level] += root.val

        if root.left: self.dfs(root.left, level + 1)
        if root.right: self.dfs(root.right, level + 1)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 1)

        res, temp = 0, float("-inf")

        for k, v in self.values.items():
            if v > temp:
                temp = v
                res = k

        return res
