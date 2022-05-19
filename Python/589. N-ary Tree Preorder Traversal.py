"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        if root:
            result.append(root.val)
            for i in root.children:
                result += self.preorder(i)
        return result
