class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            i = 0
            while True:
                if len(string) <= i: break
                if string[0] == "#": string = string[1:]
                if i > 0 and string[i] == "#":
                    string = string[:i - 1] + string[i + 1:]
                    i -= 1
                else: i+= 1
            return string

        return helper(s) == helper(t)
