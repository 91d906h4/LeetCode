# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        temp, result = 0, 0
        def dfs(node, counter):
            nonlocal temp, result
            if not node: return
            if counter > temp:
                temp = counter
                result = node.val
            elif counter == temp:
                result += node.val
            dfs(node.left, counter + 1)
            dfs(node.right, counter + 1)
        dfs(root, 0)
        return result
