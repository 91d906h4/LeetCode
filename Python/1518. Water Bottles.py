class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter = 0
        counter += numBottles
        while numBottles // numExchange >= 1:
            counter += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return counter
