class Solution:
    def judgeCircle(self, moves: str) -> bool:
#         result = [0, 0]
#         for i in moves:
#             if i == "U": result[0] += 1
#             elif i == "D": result[0] -= 1
#             elif i == "R": result[1] += 1
#             elif i == "L": result[1] -= 1
#         return result == [0, 0]

        return moves.count("U") == moves.count("D") and moves.count("R") == moves.count("L")
