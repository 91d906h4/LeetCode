class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        result = []
        for i in box:
            temp = "".join(i).split("*")
            hoge = []
            for t in temp:
                a = t.count("#")
                l = len(t)
                t = "." * (l - a) + "#" * a
                hoge.append(t)
            result.append(list("*".join(hoge)))

        return list(zip(*reversed(result)))
