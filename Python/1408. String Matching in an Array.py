class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in words:
            for j in words:
                if i != j and j in i and j not in result:
                    result.append(j)
        return result
