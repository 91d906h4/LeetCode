class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        table = {}
        spec = set() # For palindromes

        for w in words:
            t = w[::-1]

            if table.get(t, 0):
                table[t] -= 1
                res += 4
            else:
                table[w] = table.get(w, 0) + 1

            if w[0] == w[1]:
                if w in spec:
                    spec.remove(w)
                else:
                    spec.add(w)

        return res + (2 if spec else 0)
