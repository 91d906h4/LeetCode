class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        path = path.split("/")

        for i in path:
            if i == "" or i == ".": continue
            elif i == "..":
                if res: res.pop()
            else: res.append(i)

        return "/" + "/".join(res)
