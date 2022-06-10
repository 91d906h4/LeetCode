# from re import findall

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return findall('.' * k, s + fill * (k - len(s) % k if len(s) % k else 0))
