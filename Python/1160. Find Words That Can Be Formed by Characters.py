class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        for i in words:
            t = copy.deepcopy(chars)
            flag = 1

            for j in i:
                if j not in t:
                    flag = 0
                    break
                t = t.replace(j, "", 1)
            
            if flag: res += len(i)
        
        return res
