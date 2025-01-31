# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = ''

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, s):
            if not node: return

            s = chr(node.val + 97) + s

            if not node.left and not node.right:
                if not self.result or self.result > s:
                    self.result = s

                return chr(node.val + 97)

            dfs(node.left, s)
            dfs(node.right, s)

        dfs(root, '')

        return self.result
