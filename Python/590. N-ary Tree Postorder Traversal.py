"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root:
            for i in root.children:
                result += self.postorder(i)
            result.append(root.val)
        return result
