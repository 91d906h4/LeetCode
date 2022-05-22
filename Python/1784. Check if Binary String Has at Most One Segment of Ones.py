class Solution:
    def checkOnesSegment(self, s: str) -> bool:
#         return len([x for x in s.split("0") if x != ""]) == 1

        return '01' not in s
