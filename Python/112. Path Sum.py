# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        def dfs(node, total):
            if not node: return 

            total += node.val
            if not node.left and not node.right:
                print(total)
                if not self.res: self.res = total == targetSum

            if node.left: dfs(node.left, total)
            if node.right: dfs(node.right, total)

        dfs(root, 0)

        return self.res
