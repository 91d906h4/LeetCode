from collections import deque

class Solution:
    def isBipartite(self, n: int, adj: List[List[int]]) -> bool:
        color = [-1] * (n + 1)

        for i in range(1, n + 1):
            if color[i] != -1:
                continue

            color[i] = 0
            q = deque([i])

            while q:
                u = q.popleft()

                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)

                    elif color[v] == color [u]:
                        return False

        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]

        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        return self.isBipartite(n, adj)
