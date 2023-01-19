class UndergroundSystem:

    def __init__(self):
        self.t = {}
        self.stationName = {}
        self.averageTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.t[id] = t
        self.stationName[id] = stationName

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        temp = self.stationName[id] + '!' + stationName
        if temp not in self.averageTime:
            self.averageTime[temp] = []
        self.averageTime[temp].append(t - self.t[id])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        temp = self.averageTime[startStation + '!' + endStation]
        return sum(temp) / len(temp)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
