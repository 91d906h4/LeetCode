"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return
        result = []
        def helper(node):
            for n in node.children:
                helper(n)
            result.append(node.val)
        helper(root)
        return result
