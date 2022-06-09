class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # temp = len(s)
        # if temp== 2: return s[0] == s[1]
        # for i in range(2, temp):
        #     if s.count(s[:temp // i]) * (temp // i) == temp: return True
        # return False
        
        return s in (s+s)[1:-1]
