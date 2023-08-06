class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s: return s[0].lower() + "*****" + s[s.find("@") - 1].lower() + s[s.find("@"):].lower()

        t, l = "", 0
        for i in s:
            if i in "0123456789": t += i; l += 1

        if l == 10: return "***-***-" + t[-4:]
        elif l == 11: return "+*-***-***-" + t[-4:]
        elif l == 12: return "+**-***-***-" + t[-4:]
        else: return "+***-***-***-" + t[-4:]
