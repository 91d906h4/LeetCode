# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        hoge = []
        def dfs(node):
            hoge.append(node.val)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        if root: dfs(root)
        return hoge
