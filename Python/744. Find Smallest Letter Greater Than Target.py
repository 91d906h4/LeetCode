class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         letters.append(target)
#         letters.sort(reverse = True)
#         temp = letters.index(target) - 1
#         if temp < 0:
#             return letters[-1]
#         else:
#             return letters[temp]

        for i in letters:
            if i > target: return i
        return letters[0]
