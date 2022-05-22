class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for i in list("!?',;."):
            paragraph = paragraph.replace(i, " ")
        result = []
        for i in paragraph.split():
            if i not in banned: result.append(i)
        return Counter(result).most_common()[0][0]
