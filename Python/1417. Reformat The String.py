class Solution:
    def reformat(self, s: str) -> str:
        string, digit = [], []
        for i in s:
            if i.isdigit(): digit.append(i)
            else: string.append(i)
        
        l1, l2 = len(string), len(digit)
        if abs(l1 - l2) > 1: return ""
        result = ""
        for _ in range(min(l1, l2)):
            result += string.pop() + digit.pop()
        if len(string) > 0: return result + string.pop()
        elif len(digit) > 0: return digit.pop() + result
        else: return result
