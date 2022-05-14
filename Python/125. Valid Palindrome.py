import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
#         temp1, temp2 = [], []
#         for i in list(s):
#             if i.isalnum():
#                 i = i.lower()
#                 temp1.insert(0, i)
#                 temp2.append(i)
#         return temp1 == temp2

        temp = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return temp == temp[::-1]
