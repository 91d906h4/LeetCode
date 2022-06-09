class Solution:
    def detectCapitalUse(self, word: str) -> bool:
#         return word in [word.lower(), word.upper(), word.capitalize()]
    
        return word.isupper() or word.islower() or word.istitle()
