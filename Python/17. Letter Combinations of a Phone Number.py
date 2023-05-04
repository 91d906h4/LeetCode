class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = digits.replace("1", "")
        if digits == "": return []

        d = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        result = [""]

        for i in digits:
            temp = []
            for j in d[int(i)]:
                for k in result:
                    temp.append(k + j)
            result = temp

        return result
