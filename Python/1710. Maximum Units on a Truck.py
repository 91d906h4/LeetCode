class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        temp = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        result = 0
        for i, j in temp:
            if truckSize == 0: break
            elif truckSize - i >= 0:
                truckSize -= i
                result += i * j
            else:
                result += truckSize * j
                truckSize = 0
        return result
