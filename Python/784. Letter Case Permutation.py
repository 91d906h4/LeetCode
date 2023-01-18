class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        temp, res, s = [], [], s.lower()

        for i in range(len(s)):
            if s[i] not in "0123456789": temp.append(i)

        for i in range(len(temp) + 1):
            for j in combinations(temp, i):
                t = list(s)
                for k in j: t[k] = t[k].upper()
                res.append(''.join(t))

        return res
