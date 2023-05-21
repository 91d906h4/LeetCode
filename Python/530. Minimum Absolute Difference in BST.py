# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        temp = []

        def dfs(node):
            if not node: return

            if node.left: dfs(node.left)
            temp.append(node.val)
            if node.right: dfs(node.right)

        dfs(root)

        m = float("inf")

        for i in range(1, len(temp)):
            if temp[i] - temp[i - 1] < m:
                m = temp[i] - temp[i - 1]

        return m
