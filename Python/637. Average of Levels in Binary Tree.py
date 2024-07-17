# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        nodes = [root]
        result = []

        while nodes:
            counter = 0
            summation = 0
            temp = []

            while nodes:
                n = nodes.pop(0)
                counter += 1
                summation += n.val

                if n.left: temp.append(n.left)
                if n.right: temp.append(n.right)

            nodes = temp
            result.append(summation / counter)

        return result
