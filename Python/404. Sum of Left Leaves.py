# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, left = False):
            if not node: return 0
            if left and node.left is node.right: return node.val
            return dfs(node.left, True) + dfs(node.right)
        return dfs(root)
