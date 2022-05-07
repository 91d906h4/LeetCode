class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)
        result = [0] * size
        one = []
        for i in range(0, size):
            if boxes[i] == "1":
                one.append(i)
        for i in range(0, size):
            temp = 0
            for j in one:
                temp += abs(j - i)
            result[i] = temp
        return result
