class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for i in words:
            for j in i.split(separator):
                if j != "": res.append(j)

        return res
