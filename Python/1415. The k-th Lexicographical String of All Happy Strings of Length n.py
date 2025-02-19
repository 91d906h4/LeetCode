class Solution:
    def __init__(self) -> None:
        self.counter = 0
        self.result = ""

    def getHappyString(self, n: int, k: int) -> str:
        self.counter = k

        def dfs(s: str, depth: int) -> None:
            if depth == 0:
                self.counter -= 1

                if self.counter == 0:
                    self.result = s

                return

            if s == "":
                dfs("a", depth-1); dfs("b", depth-1); dfs("c", depth-1)
                return

            if s[-1] == "a":
                dfs(s + "b", depth-1); dfs(s + "c", depth-1)
            if s[-1] == "b":
                dfs(s + "a", depth-1); dfs(s + "c", depth-1)
            if s[-1] == "c":
                dfs(s + "a", depth-1); dfs(s + "b", depth-1)

        dfs("", n)

        return self.result
