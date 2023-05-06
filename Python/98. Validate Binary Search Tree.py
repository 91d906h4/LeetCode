# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []

        def inOrder(node):
            if node.left: inOrder(node.left)
            print(node.val)
            order.append(node.val)
            if node.right: inOrder(node.right)

        inOrder(root)

        for i in range(1, len(order)):
            if order[i - 1] >= order[i]: return False

        return True
