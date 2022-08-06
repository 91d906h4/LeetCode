class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         temp = [abs(ord(i) - ord(j)) for i, j in zip(s, t)]
#         a, r, m, n, k = [], 0, 0, 0, 0
#         while k < len(temp):
#             i = temp[k]
#             if r + i <= maxCost:
#                 r += i
#                 a.append(i)
#                 n += 1
#             else:
#                 if len(a) != 0:
#                     n -= 1
#                     r -= a.pop(0)
#                     k -= 1
#             k += 1
#             m = max(m, n)
#         return m

        k = 0
        for i in range(len(s)):
            maxCost -= abs(ord(s[i]) - ord(t[i]))
            if maxCost < 0:
                maxCost += abs(ord(s[k]) - ord(t[k]))
                k += 1
        return i - k + 1
