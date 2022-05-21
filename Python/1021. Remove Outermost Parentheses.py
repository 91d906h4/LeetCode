class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        trigger = 0
        for i in s:
            if i == "(":
                trigger += 1
                if trigger > 1:
                    result.append(i)
            if i == ")":
                if trigger > 1:
                    result.append(i)
                trigger -= 1
        return "".join(result)
