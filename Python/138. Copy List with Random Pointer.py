"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}

        def dfs(node):
            if not node: return
            if node in nodes: return nodes[node]

            new = Node(node.val)
            nodes[node] = new

            new.next = dfs(node.next)
            new.random = dfs(node.random)

            return new

        return dfs(head)
