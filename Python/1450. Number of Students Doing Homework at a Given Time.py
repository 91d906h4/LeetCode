class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        temp = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime and queryTime <= end: temp += 1
        return temp
