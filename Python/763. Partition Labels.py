class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # b (begin point, int): The begin point of current sub sentence.
        # c (current char, string): The current char.
        # e (end point, int): The "potential" end point of current sub sentence.
        # i (index, int): The current index.
        # r (result, list): Store the result.
        # s (string, str): The inputted string.
        # t (table, dict): Store the end point (the last index) of each chars in string s.

        t, r = {}, []

        for c in set(s):
            t[c] = s.rfind(c)

        # The begin point points to the previous index
        # of the start char of current sentense.
        # The beginning is 0, so it is initialized to -1.
        b, e = -1, 0

        for i in range(len(s)):
            if e == i == t[s[i]]:
                r.append(i - b)
                b = i
                e = i + 1
            else:
                e = max(e, t[s[i]])
        else:
            if i - b != 0:
                r.append(i - b)

        return r
