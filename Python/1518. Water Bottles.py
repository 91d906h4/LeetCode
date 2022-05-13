class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter = 0
        counter += numBottles
        while numBottles // numExchange >= 1:
            print(counter, numBottles)
            counter += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
            print(counter, numBottles)
        return counter
