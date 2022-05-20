class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = []
        for i in s:
            if i in "aeiouAEIOU": temp.append(i)
        result = ""
        for i in s:
            if i not in "aeiouAEIOU": result += i
            else: result += temp.pop()
        return result
