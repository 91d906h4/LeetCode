class Solution:
    def minSwaps(self, s: str) -> int:
#         temp = []

#         for i in s:
#             if i == "]" and temp and temp[-1] == "[": temp.pop()
#             else: temp.append(i)

#         return math.ceil(len(temp) / 4)

        temp = 0
        
        for i in s:
            if i == '[': temp += 1
            elif temp >0: temp -= 1
        
        return (temp + 1) // 2
