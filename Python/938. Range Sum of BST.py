# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def deep_first_search(root):
            if not root:
                return
            if low <= root.val <= high:
                self.result += root.val
            if low <= root.val:
                deep_first_search(root.left)
            if high >= root.val:
                deep_first_search(root.right)
        self.result = 0
        deep_first_search(root)
        return self.result
