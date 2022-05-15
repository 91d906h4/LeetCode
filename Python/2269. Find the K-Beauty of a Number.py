class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        temp, counter = str(num), 0
        for i in range(len(temp) - k + 1):
            cur = int(temp[i:i+k])
            if cur == 0: continue
            if int(temp) % cur == 0: counter += 1
        return counter
