class MedianFinder:

    def __init__(self):
        self.hoge = []

    def addNum(self, num: int) -> None:
        self.hoge.append(num)

    def findMedian(self) -> float:
        self.hoge.sort()
        fuga = len(self.hoge)
        if fuga % 2 == 0:
            fuga = len(self.hoge) // 2 - 1
            return (self.hoge[fuga] + self.hoge[fuga + 1]) / 2
        else:
            fuga = (len(self.hoge) - 1) // 2
            return self.hoge[fuga]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
