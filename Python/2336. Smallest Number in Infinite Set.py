class SmallestInfiniteSet:

    def __init__(self):
        self.temp = [0]

    def popSmallest(self) -> int:
        t = [x for x in range(1, max(self.temp) + 2)]
        t = min(set(t) - set(self.temp))
        self.temp.append(t)
        return t

    def addBack(self, num: int) -> None:
        if num in self.temp: self.temp.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
