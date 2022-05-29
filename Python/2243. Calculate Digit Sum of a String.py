class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def add(n):
            return str(sum(map(int, list(n))))

        while len(s) > k:
            hoge = [s[i:i + k] for i in range(0, len(s), k)]
            fuga = ""
            for i in hoge:
                fuga += add(i)
            s = fuga
        return s
