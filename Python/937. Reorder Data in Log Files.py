class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def helper(arr):
            arr = sorted(arr, key = lambda x: (x.split()[1:], x.split()[0]))
            return arr
        
        temp = []
        i = 0
        while i < len(logs):
            if not logs[i][-1].isdigit(): temp.append(logs.pop(i))
            else: i += 1
        return helper(temp) + logs
