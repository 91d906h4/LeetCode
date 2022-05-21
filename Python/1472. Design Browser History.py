class BrowserHistory:

    def __init__(self, homepage: str):
        self.index = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.pointer += 1
        self.index = self.index[:self.pointer]
        self.index.append(url)

    def back(self, steps: int) -> str:
        if self.pointer - steps >= 0:
            self.pointer -= steps
        else:
            self.pointer = 0
        return self.index[self.pointer]

    def forward(self, steps: int) -> str:
        if self.pointer + steps < len(self.index):
            self.pointer += steps
        else:
            self.pointer = len(self.index) - 1
        return self.index[self.pointer]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
