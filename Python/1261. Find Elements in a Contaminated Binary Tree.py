# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.s = set()
        self.s.add(0)

        def dfs(node):
            if not node: return

            if node.left:
                node.left.val = node.val * 2 + 1
                self.s.add(node.left.val)
                dfs(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                self.s.add(node.right.val)
                dfs(node.right)

        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
