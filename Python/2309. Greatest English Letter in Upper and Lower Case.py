class Solution:
    def greatestLetter(self, s: str) -> str:
        s, m = set(s), ' '

        for i in s:
            if chr(ord(i) + 32) in s and ord(i) > ord(m): m = i
        
        return m if m != ' ' else ''
