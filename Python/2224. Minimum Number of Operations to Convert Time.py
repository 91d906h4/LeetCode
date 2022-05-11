class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(":")
        current = int(current[0]) * 60 + int(current[1])
        correct = correct.split(":")
        correct = int(correct[0]) * 60 + int(correct[1])
        x = correct - current
        counter = 0
        while x > 0:
            print(x)
            if x - 60 >= 0:
                x -= 60
            elif x - 15 >= 0:
                x -= 15
            elif x - 5 >= 0:
                x -= 5
            elif x - 1 >= 0:
                x -= 1
            counter += 1
        return counter
