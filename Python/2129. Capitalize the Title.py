class Solution:
    def capitalizeTitle(self, title: str) -> str:
        temp = title.split()
        result = []
        for i in temp:
            if len(i) <= 2: result.append(i.lower())
            else: result.append(i.capitalize())
        return " ".join(result)
