# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node):
            if node.left: dfs(node.left)
            result.append(node.val)
            if node.right: dfs(node.right)
        if root: dfs(root)
        return result
