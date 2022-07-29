class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s):
            dict_ = {}
            t = 0
            r = []
            for i in s:
                if i not in dict_:
                    dict_[i] = t
                    t += 1
                r.append(dict_[i])
            return r

        return helper(s) == helper(t)
