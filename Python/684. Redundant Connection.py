class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = {}

        def root(node):
            if node not in roots:
                roots[node] = node

            if roots[node] != node:
                roots[node] = root(roots[node])

            return roots[node]

        for [a, b] in edges:
            ra, rb = root(a), root(b)

            if ra == rb:
                return [a, b]

            roots[rb] = ra

        return edges[-1]
