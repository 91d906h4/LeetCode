class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        temp = []

        for i in folder:
            t = False

            for j in temp:
                if i.startswith(j + "/"): t = True; break

            if not t: temp.append(i)

        return temp
