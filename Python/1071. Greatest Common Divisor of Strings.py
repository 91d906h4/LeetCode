class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if set(str1) != set(str2): return ""
        # for i in range(min(len(str1), len(str2)) + 1, -1, -1):
        #     if str1.replace(str1[:i], "") == str2.replace(str1[:i], "") == "": return str1[:i]
        # return ""
        
        return str1[:gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ""
