class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
#         s = s.replace("-", "").upper()[::-1]
#         result = ""
#         for i in range(len(s)):
#             if i % k == 0 and i != 0: result = "-" + result
#             result = s[i] + result
#         return result

        s = s.replace("-", "").upper()[::-1]
        result = ""
        for i in range(0, len(s), k):
            result += s[i:i+k] + "-"
        result = result[:len(result) - 1]
        return result[::-1]
