class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("!")
        t1, t2, l = 1, "", len(chars) + 1
        for i in chars:
            if i == "": break
            if t2 == i: t1 += 1
            else:
                chars.append(t2)
                if t1 != 1: chars += list(str(t1))
                t1, t2 = 1, i
        chars[:] = chars[l:]
        return len(chars)
