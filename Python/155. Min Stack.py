class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return min(self.stack)

    def __init__(self):
        self.stack, self.min = [], []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0 or val <= self.min[-1]: self.min.append(val)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.min[-1]: self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
