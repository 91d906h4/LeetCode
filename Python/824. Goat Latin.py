class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result, temp = [], 1
        for i in sentence.split():
            if i[0] in "aeiouAEIOU": n = i + "ma"
            else:
                n = i[1:] + i[0] + "ma"
            result.append(n + ("a" * temp))
            temp += 1
        return " ".join(result)
