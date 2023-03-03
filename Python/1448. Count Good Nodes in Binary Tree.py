# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, m):
            if not node: return

            if node.val >= m: self.res += 1
            m = max(m, node.val)

            if node.left: dfs(node.left, m)
            if node.right: dfs(node.right, m)

        dfs(root, -10001)

        return self.res
