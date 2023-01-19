class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.com = list(combinations(characters, combinationLength))
        self.ptr = -1
        self.l = len(self.com)

    def next(self) -> str:
        self.ptr += 1
        return ''.join(self.com[self.ptr])

    def hasNext(self) -> bool:
        return self.ptr < self.l - 1


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
