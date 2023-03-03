# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l = []

        def dfs(node):
            if node: l.append(node.val)
            else: return

            if node.left: dfs(node.left)
            if node.right: dfs(node.right)

        dfs(root1)
        dfs(root2)

        return sorted(l)
