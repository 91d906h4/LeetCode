class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = abs(tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x
        return [x, y] if 4 * x + 2 * y == tomatoSlices and x + y == cheeseSlices and x >= 0 and y >= 0 else []
