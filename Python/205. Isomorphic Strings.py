class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s):
            dict_, r, t = {}, [], 0
            for i in s:
                if i not in dict_:
                    dict_[i] = t
                    t += 1
                r.append(dict_[i])
            return r

        return helper(s) == helper(t)
