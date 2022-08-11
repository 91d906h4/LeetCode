class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ra, dict_ = 0, Counter()
        s, g = Counter(secret), Counter(guess)
        for i in s:
            if i not in g: continue
            dict_[i] = min(s[i], g[i]) * 2

        for s, g in zip(secret, guess):
            if s == g:
                ra += 1
                dict_[i] -= 2

        return str(ra) + "A" + str(sum(dict_.values()) // 2) + "B"
