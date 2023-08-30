class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r, b = 0, 0, 0

        for i in moves:
            if i == "L": l += 1
            elif i == "R": r += 1
            else: b += 1

        return abs(l - r) + b
