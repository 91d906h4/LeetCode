class MyLinkedList:

    def __init__(self):
        self.t = []

    def get(self, index: int) -> int:
        return self.t[index] if index < len(self.t) else -1

    def addAtHead(self, val: int) -> None:
        self.t.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.t.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.t): self.t.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.t): del self.t[index]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
