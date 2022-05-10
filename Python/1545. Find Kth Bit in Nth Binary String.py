class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            result = []
            for i in range(0, len(s)):
                if s[i] == "0":
                    result.append("1")
                else:
                    result.append("0")
            return "".join(reversed(result))
        dir_ = {}
        dir_[1] = "0"
        dir_[2] = "011"
        for i in range(2, n + 1):
            dir_[i] = dir_[i-1] + "1" + invert(dir_[i-1])
        return dir_[n][k-1]
