class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_before, a_after = 0, s.count("a")
        result = a_after - (1 if s[0] == "a" else 0)

        for c in s:
            if c == "a": a_after -= 1
            else: b_before += 1

            result = min(result, a_after + b_before)

        return result
