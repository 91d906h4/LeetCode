class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result, temp, i = 0, capacity, 0
        while i < len(plants):
            if plants[i] > temp:
                result += 2 * i
                temp = capacity
            else:
                temp -= plants[i]
                result += 1
                i += 1
        return result
