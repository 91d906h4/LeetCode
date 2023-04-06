# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = ""

    def dfs(self, node) -> None:
        if not node: return

        self.res += str(node.val)

        if node.left:
            self.res += "("
            self.dfs(node.left)
            self.res += ")"

        if node.right:
            if not node.left: self.res += "()"
            self.res += "("
            self.dfs(node.right)
            self.res += ")"

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.dfs(root)
        return self.res
