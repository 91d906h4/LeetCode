class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return len([x for x in s[:len(s) // 2] if x in "aeiouAEIOU"]) == len([x for x in s[len(s) // 2:] if x in "aeiouAEIOU"])
